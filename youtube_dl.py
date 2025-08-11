import argparse
import yt_dlp
import load_meta


def main():
    """
    Parses command-line arguments to download YouTube content using yt_dlp.
    Supported options:
    -v : Download the best available video in MP4 format (includes audio).
    -a : Download the best available audio and convert it to MP3.
    -s : Download English subtitles (both manual and automatic).
    If no flags are provided, displays metadata for the specified YouTube URL.
    Downloads are saved with the video title as the filename.
    Displays metadata after download and indicates which content types were downloaded.
    """

    parser = argparse.ArgumentParser(description='Download YouTube content with yt_dlp')
    parser.add_argument('url', help='YouTube video URL')
    parser.add_argument('-v', action='store_true', help='Download best video in mp4')
    parser.add_argument('-a', action='store_true', help='Download best audio')
    parser.add_argument('-s', action='store_true', help='Download subtitles')
    args = parser.parse_args()

    # If no flags, just show metadata
    if not (args.v or args.a or args.s):
        with yt_dlp.YoutubeDL({}) as ydl:
            info = ydl.extract_info(args.url, download=False)
            load_meta.show_meta(info)
        return

    ydl_opts = {'outtmpl': '%(title)s.%(ext)s'}

    # Handle subtitles options if requested
    if args.s:
        ydl_opts['writesubtitles'] = True
        ydl_opts['writeautomaticsub'] = True
        ydl_opts['subtitleslangs'] = ['en']
        # ydl_opts['subtitlesformat'] = 'srt'

    # Only subtitle
    if args.s and not (args.v or args.a):
        ydl_opts['skip_download'] = True

    # Audio only
    elif args.a and not args.v:
        ydl_opts['format'] = 'bestaudio/best'
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
        
    # Video (with audio)
    elif args.v:
        ydl_opts['format'] = 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'
        
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(args.url, download=True)
        load_meta.show_meta(result)

        print('>> Downloaded Video : ', 'OK' if args.v else 'None')
        print('>> Downloaded Audio : ', 'OK' if args.a else 'None')
        print('>> Downloaded Subtitle : ', 'OK' if args.s else 'None')


if __name__ == '__main__':
	main()
