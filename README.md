# Audio Extractor Py 🎵

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)

> **⚠️ ARCHIVED**: This repository is no longer actively maintained. It uses `youtube_dl` which may be outdated. Consider using `yt-dlp` for modern projects.

A lightweight Python library that extracts direct audio stream URLs and comprehensive video metadata from YouTube. Designed specifically for Discord bots and audio streaming applications.

## Features

- 🎯 Extract direct audio stream URLs from YouTube
- 📊 Retrieve comprehensive video metadata (title, author, views, duration, etc.)
- ⚡ Fast and lightweight
- 🎮 Perfect for Discord music bots
- 🔍 Smart search integration with YouTube

## Installation

```bash
pip install audioextractor
```

## Quick Start

```python
import audioextractor as a

# Extract formatted track information
song_name = "Sakhiyaan"
track_data = a.extract_info(song_name)
print(track_data)

# Extract raw YouTube data
raw_track_data = a.extract_raw_info(song_name)
print(raw_track_data)
```

## API Reference

### `extract_info(search_term)`

Returns formatted track data including:

- `video_id` - YouTube video ID
- `title` - Video title
- `description` - Video description
- `author` - Channel name
- `author_link` - Channel URL
- `duration` - Duration in seconds
- `human_duration` - Human-readable duration (e.g., "3 minutes, 45 seconds")
- `stream_url` - Direct audio stream URL
- `views` - View count
- `date` - Upload date
- `thumbnail` - Thumbnail URL
- `channel` - Channel information
- `tags` - Video tags
- `url` - Video webpage URL
- `likes` - Like count
- `dislikes` - Dislike count

**Returns:** Dictionary with formatted data or `False` on error

### `extract_raw_info(search_term)`

Returns raw YouTube data from youtube_dl.

**Returns:** Raw dictionary from youtube_dl or `False` on error

## Example Output

```python
{
    "Data": [
        {
            "video_id": "BvJlLAVPkKQ",
            "title": "Sakhiyaan",
            "author": "Music Channel",
            "duration": 225,
            "human_duration": "3 minutes, 45 seconds",
            "stream_url": "https://...",
            "views": 1000000,
            "thumbnail": "https://...",
            # ... more fields
        }
    ]
}
```

## Use Cases

- 🎵 Discord music bots
- 📻 Audio streaming applications
- 🔊 Podcast downloaders
- 🎼 Music metadata retrieval
- 🎧 Custom audio players

## Requirements

- Python >= 3.6
- youtube_dl

## Limitations

⚠️ **Note**: This package uses `youtube_dl` which may have compatibility issues with recent YouTube changes. For production applications, consider using [`yt-dlp`](https://github.com/yt-dlp/yt-dlp) as an alternative.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**DARKPOISON04**

## Archive Notice

This repository has been archived and is no longer maintained. It was created in January 2022 and served as a learning project for YouTube data extraction. Feel free to fork and adapt for your own projects!

## Contributing

As this repository is archived, contributions are no longer accepted. However, you're free to fork and continue development on your own fork.

---

*Made with ❤️ for the Discord bot community*
