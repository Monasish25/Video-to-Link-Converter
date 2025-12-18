# 🎬 Video-to-Link-Converter

A Python-based automation tool that monitors a folder for video files and automatically uploads them to **Catbox.moe**, generating shareable direct links for easy video sharing.

## 📖 What Does This Do?

This tool simplifies video sharing by:
1. **Monitoring** a designated folder (`files/`) for new video files
2. **Automatically uploading** detected videos to Catbox.moe (a free file hosting service)
3. **Generating shareable links** that you can use anywhere
4. **Moving processed files** to a `done/` folder to keep things organized

Perfect for quickly sharing videos without manually uploading them to hosting services!

## ✨ Features

- 🔄 **Automatic Monitoring**: Continuously watches the `files/` folder for new videos
- 📊 **Real-time Progress Bar**: See upload progress with percentage and bytes transferred
- 🔁 **Smart Retry Logic**: Automatically retries failed uploads up to 3 times
- 📁 **Auto-Organization**: Moves uploaded files to `files/done/` folder
- 🎥 **Multiple Format Support**: Works with `.mp4`, `.avi`, `.mov`, and `.mkv` files
- ⚡ **Fast & Reliable**: Uses Catbox.moe with 200MB file size limit per upload

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher
- Internet connection

### Installation

1. **Clone this repository**:
   ```bash
   git clone https://github.com/Monasish25/Video-to-Link-Converter.git
   cd Video-to-Link-Converter
   ```

2. **Install required dependencies**:
   ```bash
   pip install requests requests-toolbelt urllib3
   ```

### Usage

1. **Run the script**:
   ```bash
   python link.py
   ```

2. **Drop video files** into the `files/` folder that gets created

3. **Get your links!** The script will:
   - Detect the new video file
   - Upload it to Catbox.moe with a progress bar
   - Display the shareable link in the console
   - Move the file to `files/done/` folder

4. **Stop the script** by pressing `Ctrl+C`

## 📋 Example Output

```
Monitoring 'files/' for new videos...
Service: Catbox.moe (Max 200MB per file)
Press Ctrl+C to stop.

Found: my_video.mp4
   Attempt 1/3: Preparing upload...
   Uploading: 100.00% (52428800/52428800 bytes)
✅ Success! Link: https://files.catbox.moe/abc123.mp4
Moved to 'done' folder.
------------------------------
```

## 🛠️ Technical Details

### Supported Video Formats
- `.mp4` - MPEG-4 Video
- `.avi` - Audio Video Interleave
- `.mov` - QuickTime Movie
- `.mkv` - Matroska Video

### File Size Limit
- Maximum: **200MB per file** (Catbox.moe limitation)

### Retry Mechanism
- Automatic retries on connection failures
- Up to 3 attempts per file
- Exponential backoff between retries
- Handles timeouts and server errors (500, 502, 503, 504)

### Folder Structure
```
Video-to-Link-Converter/
├── link.py              # Main script
├── files/               # Drop videos here (auto-created)
│   └── done/           # Uploaded videos moved here (auto-created)
└── README.md
```

## 🔧 Dependencies

- **requests**: HTTP library for API calls
- **requests-toolbelt**: Provides multipart upload with progress tracking
- **urllib3**: HTTP client with retry capabilities

## ⚠️ Troubleshooting

### "Connection failed" error
- Check your internet connection
- The script will automatically retry up to 3 times

### "Timeout" error
- Your file might be too large or internet too slow
- Try with a smaller file or better connection

### Video not detected
- Make sure the file extension is `.mp4`, `.avi`, `.mov`, or `.mkv`
- Check that the file is directly in the `files/` folder, not in a subfolder

### File size too large
- Catbox.moe has a 200MB limit
- Compress your video or use a different hosting service

## 📝 License

This project is open source and available for anyone to use and modify.

## 🤝 Contributing

Feel free to fork this repository and submit pull requests for improvements!

## 💡 Use Cases

- Quickly share gameplay recordings
- Send video files to friends without email attachments
- Create shareable links for social media
- Backup videos to the cloud with direct access links
- Share tutorial videos or presentations

## 🔗 About Catbox.moe

Catbox.moe is a free file hosting service that:
- Doesn't require registration
- Provides permanent links
- Supports direct video playback
- Has no bandwidth limits

---

**Made with ❤️ for easy video sharing**
