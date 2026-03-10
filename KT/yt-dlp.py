import yt_dlp

def download_video(url):
    ydl_opts = {
        'format': 'bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]',
        'merge_output_format': 'mp4',
        'outtmpl': '%(title)s.%(ext)s',
        'extractor_args': {
            'youtube': {
                'player_client': ['android', 'web'],
            }
        },
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

video_url = input("Enter the YouTube URL: ")
download_video(video_url)
