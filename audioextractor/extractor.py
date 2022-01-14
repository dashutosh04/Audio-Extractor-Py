import youtube_dl

ytdl = youtube_dl.YoutubeDL(
    {
        "format": "bestaudio/best",
        "extractaudio": True,
        "audioformat": "mp3",
        "outtmpl": "%(extractor)s-%(id)s-%(title)s.%(ext)s",
        "restrictfilenames": True,
        "noplaylist": True,
        "nocheckcertificate": True,
        "ignoreerrors": False,
        "logtostderr": False,
        "quiet": True,
        "no_warnings": False,
        "default_search": "auto_warning",
        "source_address": "0.0.0.0",
    }
)


def _parse_duration(duration: int):
    minutes, seconds = divmod(duration, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)

    duration = []
    if days > 0:
        duration.append("{} days".format(days))
    if hours > 0:
        duration.append("{} hours".format(hours))
    if minutes > 0:
        duration.append("{} minutes".format(minutes))
    if seconds > 0:
        duration.append("{} seconds".format(seconds))

    return ", ".join(duration)


def extract_raw_info(search_term, ytdl=ytdl):
    try:
        data = ytdl.extract_info("ytsearch:%s" % search_term, download=False)
        return data
    except Exception:
        return False


def extract_info(search_term, ytdl=ytdl):
    try:
        data = ytdl.extract_info("ytsearch:%s" % search_term, download=False)[
            "entries"
        ][0]
        return {
            "Data": [
                {
                    "video_id": data["id"],
                    "title": data.get("title"),
                    "description": data.get("description"),
                    "author": data.get("uploader"),
                    "author_link": data.get("uploader_url"),
                    "duration": int(data.get("duration")),
                    "human_duration": _parse_duration(int(data.get("duration"))),
                    "stream_url ": data.get("url"),
                    "stream_duration": int(data.get("duration")),
                    "views": data.get("view_count"),
                    "date": data.get("upload_date"),
                    "human_date ": data.get("upload_date")[6:8]
                    + "."
                    + data.get("upload_date")[4:6]
                    + "."
                    + data.get("upload_date")[0:4],
                    "thumbnail ": data.get("thumbnail"),
                    "channel": data.get("channel"),
                    "tags ": data.get("tags"),
                    "url ": data.get("webpage_url"),
                    "likes ": data.get("like_count"),
                    "dislikes ": data.get("dislike_count"),
                }
            ]
        }
    except Exception:
        return False
