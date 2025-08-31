# YouTube Subtitles OAuth2 Setup Guide

This guide explains how to set up OAuth2 authentication for the `get_youtube_subtitles_oauth.py` script.

## Why OAuth2?

The YouTube Data API v3 requires OAuth2 authentication for the `captions.download` endpoint. API keys alone are not sufficient, which is why you're getting the "API keys are not supported by this API" error.

## Setup Steps

### 1. Install Required Packages

```bash
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

### 2. Create OAuth2 Credentials

1. Go to the [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the YouTube Data API v3:
   - Navigate to "APIs & Services" > "Library"
   - Search for "YouTube Data API v3"
   - Click on it and press "Enable"
4. Create OAuth2 credentials:
   - Navigate to "APIs & Services" > "Credentials"
   - Click "Create Credentials" > "OAuth 2.0 Client IDs"
   - If prompted, configure the OAuth consent screen:
     - Choose "External" user type
     - Fill in required fields (App name, User support email, Developer email)
     - Add your email to test users
   - For application type, select "Desktop application"
   - Give it a name (e.g., "YouTube Subtitle Extractor")
   - Click "Create"
5. Download the JSON credentials file and save it as `credentials.json` in the same directory as the script

### 3. Usage Examples

```bash
# List available captions
python get_youtube_subtitles_oauth.py "https://www.youtube.com/watch?v=VIDEO_ID" --list-only

# Download subtitles in SRT format
python get_youtube_subtitles_oauth.py "https://www.youtube.com/watch?v=VIDEO_ID" --output subtitles.srt

# Download subtitles in specific language
python get_youtube_subtitles_oauth.py "https://www.youtube.com/watch?v=VIDEO_ID" --language en --output english_subtitles.srt

# Download in VTT format
python get_youtube_subtitles_oauth.py "https://www.youtube.com/watch?v=VIDEO_ID" --format vtt --output subtitles.vtt
```

## First Run Authentication

On your first run, the script will:
1. Open your web browser
2. Ask you to sign in to Google
3. Ask for permission to access YouTube on your behalf
4. Save the authentication token to `token.pickle` for future use

## Troubleshooting

### "Authentication error" or 401 errors
- Delete the `token.pickle` file and run the script again to re-authenticate
- Make sure your OAuth2 consent screen is properly configured

### "The OAuth client was not found"
- Verify that `credentials.json` is in the same directory as the script
- Check that the credentials file was downloaded correctly from Google Cloud Console

### "Access blocked: This app's request is invalid"
- Make sure you've enabled the YouTube Data API v3 in your Google Cloud project
- Verify your OAuth consent screen is properly configured

## Files Created

- `credentials.json` - Your OAuth2 client credentials (keep this secure)
- `token.pickle` - Cached authentication tokens (automatically created)

## Security Notes

- Keep your `credentials.json` file secure and don't share it publicly
- The `token.pickle` file contains your access tokens - treat it as sensitive data
- Consider adding both files to your `.gitignore` if using version control