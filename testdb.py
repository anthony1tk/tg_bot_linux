from yt_dlp import YoutubeDL

with YoutubeDL() as ydl:
    info = ydl.extract_info("https://www.instagram.com/reel/DDpucvlPETs/?igsh=dnk0b2g5bW9lNjJz", download=True)
