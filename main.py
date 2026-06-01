import webbrowser
from pathlib import Path
import re
from urllib.parse import urlparse
import eel
import yt_dlp as y
from error import get_error
from get_ffmpeg import get_ffmpeg_path
from proxy import get_proxy

eel.init("web")


def is_url(url):
    parsed = urlparse(url)
    return bool(parsed.scheme and parsed.netloc)


# def progress_hook(d):
#     if d['status'] == 'downloading':
#         percent = d.get('_percent_str', '0%')
#
#         eel.update_progress(percent)


@eel.expose
def prepare_download(url, quality):
    try:
        if url == "test":
            return {"success": True}
        if not is_url(url):
            return {"success": False, "error": "E-7001 (Ссылка не поддерживается.)"}

        if not quality:
            return {"success": False, "error": "E-4002 (Не найдено доступных форматов.)"}

        if not any(x in url for x in ['youtube', 'youtu', 'pinterest', 'pin']):
            return {"success": False, "error": "E-7001 (Ссылка не поддерживается.)"}

        return {"success": True}

    except Exception as e:
        code, desc = get_error(str(e))
        return {"success": False, "error": f"{code} ({desc})"}


@eel.expose
def download_video(url, quality: str):
    try:
        downloads = str(Path.home() / "Downloads")
        ffmpeg = get_ffmpeg_path()
        height = int(re.search(r'\d+', quality).group())
        proxy = get_proxy()

        opts = None

        if any(x in url for x in ['youtube', 'youtu']):

            opts = {
                "outtmpl": f'{downloads}/%(title)s.%(ext)s',
                "format": f"bv*[height<={height}]+ba[ext=m4a]/bv*+ba[ext=m4a]/bv*+ba",
                'noplaylist': True,
                'quiet': False,
                'geo_bypass': True,
                "retries": 3,
                "fragment_retries": 10,
                "http_headers": {
                    "User-Agent": "Mozilla/5.0"
                },
                "merge_output_format": "mp4",
                "ffmpeg_location": ffmpeg,
                "postprocessors": [
                    {
                        "key": "FFmpegVideoConvertor",
                        "preferedformat": "mp4"
                    }
                ],
                "postprocessor_args": [
                    "-c:v", "copy",
                    "-c:a", "aac",
                    "-b:a", "192k",
                    "-movflags", "+faststart"
                ],
                "nopart": False,
                "overwrites": False,
                # "proxy": proxy,
                # "progress_hooks": [progress_hook],
            }

        elif any(x in url for x in ['pinterest', 'pin']):
            opts = {
                "outtmpl": f'{downloads}/%(title)s.%(ext)s',
                "noplaylist": True,
                "merge_output_format": "mp4",
                "retries": 10,
                "fragment_retries": 10,
                "http_headers": {
                    "User-Agent": "Mozilla/5.0"
                },
                "quiet": False,
                "ffmpeg_location": ffmpeg,
            }

        if opts is None:
            return {"success": False, "error": "E-7001 (Unsupported URL)"}

        try:
            with y.YoutubeDL(opts) as ydl:
                ydl.download([url])
        except y.DownloadError as e:
            code, desc = get_error(str(e))
            return {"success": False, "error": f"{code} ({desc})"}

        return {"success": True}
    except Exception as e:
        code, desc = get_error(str(e))
        return {"success": False, "error": f"{code} ({desc})"}


@eel.expose
def open_tab(url):
    webbrowser.open_new_tab(url)


eel.start(
    "index.html",
    disable_cache=True,
    size=(1000, 500)
)