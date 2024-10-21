# Load Library
import yt_dlp
conf_dl = {
    'format': 'best',
    'outtmpl': 'video.mp4',
    'quiet': True
}

class DownloadFrom:
    @staticmethod
    def Video(VidUrl):
        try:
            if "vt.tiktok.com" or "tiktok.com" in VidUrl:
                with yt_dlp.YoutubeDL(conf_dl) as ydl:
                    ydl.download([VidUrl])
            elif "youtube.com" in VidUrl:
                with yt_dlp.YoutubeDL(conf_dl) as ydl:
                    ydl.download([VidUrl])
            elif "instagram.com" or "https://www.instagram.com/reel" in VidUrl:
                with yt_dlp.YoutubeDL(conf_dl) as ydl:
                    ydl.download([VidUrl])
            else:
                with yt_dlp.YoutubeDL(conf_dl) as ydl:
                    ydl.download([VidUrl])
        except:
            print(f"Unable To Download Video From Links: {VidUrl}")