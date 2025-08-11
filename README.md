# tool-youtube

A command-line tool for downloading YouTube videos, audio, and subtitles using Python and yt-dlp.

## Features
- Download best video in MP4 format (with audio)
- Download best audio in MP3 format
- Download English subtitles in SRT format
- Print rich metadata for any YouTube video
- Flexible flag combinations for custom downloads


## Requirements
- Python 3.7+
- Required Python packages: Install with
	```sh
	pip install -r requirements.txt
	```
- ffmpeg (for best quality and format conversion)
- macOS: Install ffmpeg with Homebrew:
	```sh
	brew install ffmpeg
	```

### How to install Homebrew (macOS)
If you don't have Homebrew, open Terminal and run:
```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
See the official guide: [brew.sh](https://brew.sh)

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
