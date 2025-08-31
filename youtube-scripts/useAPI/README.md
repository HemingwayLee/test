# YouTube Subtitle Extractor

A Python script to extract subtitles from YouTube videos using the YouTube Data API v3.

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Get YouTube Data API v3 Key:**
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project or select an existing one
   - Enable the YouTube Data API v3
   - Create credentials (API Key)
   - Restrict the API key to YouTube Data API v3 for security

## Usage

### Basic Usage
```bash
python get_youtube_subtitles.py "VIDEO_URL_OR_ID" --api-key "YOUR_API_KEY"
```

### Examples

**Extract subtitles from a YouTube video:**
```bash
python get_youtube_subtitles.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" --api-key "YOUR_API_KEY"
```

**Save subtitles to a file:**
```bash
python get_youtube_subtitles.py "dQw4w9WgXcQ" --api-key "YOUR_API_KEY" --output "subtitles.srt"
```

**Specify language:**
```bash
python get_youtube_subtitles.py "VIDEO_URL" --api-key "YOUR_API_KEY" --language "es"
```

**Choose format:**
```bash
python get_youtube_subtitles.py "VIDEO_URL" --api-key "YOUR_API_KEY" --format "vtt"
```

**List available captions only:**
```bash
python get_youtube_subtitles.py "VIDEO_URL" --api-key "YOUR_API_KEY" --list-only
```

### Options

- `--api-key`: Your YouTube Data API v3 key (required)
- `--language`: Language code (e.g., 'en', 'es', 'fr', 'de')
- `--format`: Subtitle format - 'srt' (default), 'vtt', or 'ttml'
- `--output`: Output file path
- `--list-only`: Only list available captions without downloading

### Supported Input Formats

- Full YouTube URLs: `https://www.youtube.com/watch?v=VIDEO_ID`
- Short URLs: `https://youtu.be/VIDEO_ID`
- Embed URLs: `https://www.youtube.com/embed/VIDEO_ID`
- Video ID only: `VIDEO_ID`

## Features

- Extracts both auto-generated and manual captions
- Supports multiple subtitle formats (SRT, VTT, TTML)
- Language selection
- Lists all available caption tracks
- Error handling for common issues
- Video information display

## Limitations

- Requires YouTube Data API v3 key (free but with quotas)
- Some videos may have caption downloads disabled by the owner
- API quota limits apply (10,000 units/day by default)

## Error Handling

The script handles common errors such as:
- Invalid video URLs/IDs
- Videos without captions
- Disabled caption downloads
- API quota exceeded
- Network errors