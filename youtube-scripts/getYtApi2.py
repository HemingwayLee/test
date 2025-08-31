import requests
import re
import json

def get_youtube_subtitles(youtube_url):
    """
    Fetches available subtitle languages from a YouTube video URL.
    
    Args:
        youtube_url (str): The full URL of the YouTube video.
        
    Returns:
        list or None: A list of dictionaries with 'language' and 'code' 
                      if subtitles are found, otherwise None.
    """
    try:
        # Send a GET request to the YouTube video URL
        response = requests.get(youtube_url)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Find the JSON object containing player data
        # We use a regular expression to find the 'ytInitialPlayerResponse' variable
        pattern = r"var ytInitialPlayerResponse = ({.*?});"
        match = re.search(pattern, response.text)

        if not match:
            print("Could not find player data in the HTML.")
            return None

        # Extract the JSON string and parse it
        player_data_str = match.group(1)
        player_data = json.loads(player_data_str)

        # Navigate to the captions data
        captions = player_data.get('captions', {})
        if not captions:
            print("No 'captions' key found in player data.")
            return None
            
        tracklist_renderer = captions.get('playerCaptionsTracklistRenderer', {})
        if not tracklist_renderer:
            print("No 'playerCaptionsTracklistRenderer' found.")
            return None
        
        caption_tracks = tracklist_renderer.get('captionTracks', [])

        if not caption_tracks:
            print("No subtitle tracks available for this video.")
            return []

        # Extract language name and code for each track
        subtitle_languages = [
            {
                "language": track['name']['simpleText'],
                "code": track['languageCode']
            }
            for track in caption_tracks
        ]

        return subtitle_languages

    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the request: {e}")
        return None
    except (json.JSONDecodeError, KeyError) as e:
        print(f"An error occurred while parsing the JSON: {e}")
        return None

# Example usage:
if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=Bg8_h6Bt1VI"  # Rick Astley's "Never Gonna Give You Up"
    subtitles = get_youtube_subtitles(video_url)

    if subtitles:
        print("Available Subtitle Languages:")
        for lang in subtitles:
            print(f"- {lang['language']} ({lang['code']})")
    elif subtitles is not None:
        print("No subtitles found.")
    else:
        print("Failed to retrieve subtitle information.")
