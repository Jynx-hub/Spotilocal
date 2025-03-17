import yt_dlp
import sys
import os

def download_mp3(youtube_url, output_template):
    # Ensure the temp directory exists
    os.makedirs(os.path.dirname(output_template), exist_ok=True)
    
    # Options for downloading best audio and post-processing to mp3 using FFmpeg
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_template,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        # Optional: Suppress output messages (set to False to see more details)
        'quiet': False,
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python mp3.py <url> <output_template>")
        sys.exit(1)
        
    url = sys.argv[1].strip()
    output_template = sys.argv[2].strip()
    
    try:
        download_mp3(url, output_template)
        print("Download and conversion to MP3 complete!")
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
