import requests
import os
import time
import shutil
import sys
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
# New dependency for progress bar
from requests_toolbelt import MultipartEncoder, MultipartEncoderMonitor 

def upload_to_catbox(file_path, max_retries=3):
    """
    Uploads file to Catbox.moe with a progress bar.
    """
    url = "https://catbox.moe/user/api.php"
    
    # Retry strategy
    session = requests.Session()
    retry_strategy = Retry(
        total=max_retries,
        backoff_factor=2,
        status_forcelist=[500, 502, 503, 504],
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("https://", adapter)
    session.mount("http://", adapter)

    # Define the progress callback function
    def progress_callback(monitor):
        # Calculate percentage
        percent = (monitor.bytes_read / monitor.len) * 100
        # Use \r to overwrite the same line on the console
        sys.stdout.write(f"\r   Uploading: {percent:.2f}% ({monitor.bytes_read}/{monitor.len} bytes)")
        sys.stdout.flush()

    for attempt in range(1, max_retries + 1):
        try:
            # Open file in binary mode
            with open(file_path, 'rb') as f:
                print(f"   Attempt {attempt}/{max_retries}: Preparing upload...")

                # 1. Create a MultipartEncoder
                # This explicitly builds the multipart form data so we can track its size
                encoder = MultipartEncoder(
                    fields={
                        'reqtype': 'fileupload',
                        'fileToUpload': (os.path.basename(file_path), f, 'application/octet-stream')
                    }
                )

                # 2. Create the Monitor
                # This wraps the encoder and calls our callback every time bytes are read
                monitor = MultipartEncoderMonitor(encoder, progress_callback)

                # 3. Send the request
                # Note: We pass the 'monitor' to data= and set the headers manually
                response = session.post(
                    url, 
                    data=monitor, 
                    headers={'Content-Type': monitor.content_type}, 
                    timeout=600
                )
                
                # Print a newline to move off the progress bar line
                print("") 

                if response.status_code == 200:
                    return True, response.text.strip()
                else:
                    print(f"   ❌ Server Error: {response.status_code}")

        except requests.exceptions.ConnectionError:
            print(f"\n   ⚠️ Connection failed on attempt {attempt}.")
        except requests.exceptions.Timeout:
            print(f"\n   ⚠️ Timeout (upload took too long) on attempt {attempt}.")
        except Exception as e:
            print(f"\n   ⚠️ Error: {e}")
        
        time.sleep(3) 
    
    return False, None

def watch_and_upload():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    source_folder = os.path.join(script_dir, 'files')
    done_folder = os.path.join(script_dir, 'files', 'done')

    if not os.path.exists(source_folder):
        os.makedirs(source_folder)
        print(f"Created folder: {source_folder}")
    if not os.path.exists(done_folder):
        os.makedirs(done_folder)

    print(f"Monitoring '{source_folder}' for new videos...")
    print("Service: Catbox.moe (Max 200MB per file)")
    print("Press Ctrl+C to stop.\n")

    try:
        while True:
            files = os.listdir(source_folder)
            video_files = [
                f for f in files 
                if f.lower().endswith(('.mp4', '.avi', '.mov', '.mkv')) 
                and os.path.isfile(os.path.join(source_folder, f))
            ]

            if video_files:
                for file_name in video_files:
                    file_path = os.path.join(source_folder, file_name)
                    print(f"Found: {file_name}")

                    success, link = upload_to_catbox(file_path)

                    if success:
                        print(f"✅ Success! Link: {link}")
                        try:
                            shutil.move(file_path, os.path.join(done_folder, file_name))
                            print(f"Moved to 'done' folder.")
                        except Exception as move_err:
                            print(f"⚠️ Uploaded, but failed to move file: {move_err}")
                    else:
                        print(f"❌ Failed to upload {file_name} after multiple attempts.")
                    
                    print("-" * 30)
            
            time.sleep(5)

    except KeyboardInterrupt:
        print("\nStopping.")

if __name__ == "__main__":
    watch_and_upload()