# tool-youtube

A command-line tool for downloading YouTube videos, audio, and subtitles using Python and yt-dlp.

## Features
- Download best video in MP4 format (with audio)
- Download best audio in MP3 format
- Download English subtitles in SRT format
- Print rich metadata for any YouTube video
- Flexible flag combinations for custom downloads



## Getting Started (Step-by-Step for Beginners)

### 1. Install Git
If you don't have git, download and install it from:
- [Git for Windows](https://git-scm.com/download/win)
- [Git for macOS](https://git-scm.com/download/mac)
- [Git for Linux](https://git-scm.com/download/linux)

### 2. Clone this Repository
Open Terminal (or Command Prompt on Windows) and run:
```sh
git clone https://github.com/o0fung/tool-youtube.git
cd tool-youtube
```

### 3. Install Homebrew (macOS only)
If you don't have Homebrew, open Terminal and run:
```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
See the official guide: [brew.sh](https://brew.sh)

### 4. Install ffmpeg
- **macOS:**
	```sh
	brew install ffmpeg
	```
- **Windows:** Download from [ffmpeg.org/download.html](https://ffmpeg.org/download.html) and follow the instructions.
- **Linux:**
	```sh
	sudo apt-get install ffmpeg
	```

### 5. Install Python Packages
Make sure you have Python 3.7 or newer. Then run:
```sh
pip install -r requirements.txt
```

## Usage
```sh
python youtube_dl.py <URL> [flags]
```

### Flags
- `-v` : Download best video in mp4 (includes audio)
- `-a` : Download best audio in mp3
- `-s` : Download English subtitles (SRT)

Flags can be combined:
- No flags: Only print metadata
- `-s` : Only download subtitles
- `-a` : Only download audio (mp3)
- `-v` : Only download video (mp4 with audio)
- `-vs` : Download video (mp4 with audio) and subtitles

## Example
```sh
python youtube_dl.py "https://www.youtube.com/watch?v=H7cIkLZH8UA" -vs
```

## Output
- Downloads are saved with the video title as the filename
- Metadata is printed after each operation

## Project Structure
- `youtube_dl.py` : Main script for downloading and printing metadata
- `load_meta.py` : Helper for formatting and printing metadata

## License
MIT
