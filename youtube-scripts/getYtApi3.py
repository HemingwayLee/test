import requests
import re
import json
import xml.etree.ElementTree as ET

def get_youtube_subtitles(youtube_url):
    """
    Fetches the subtitle text for the first available language from a YouTube URL.
    
    Args:
        youtube_url (str): The full URL of the YouTube video.
        
    Returns:
        str or None: The parsed subtitle text, or None if no subtitles are found or an error occurs.
    """
    try:
        # Step 1: Get the video page HTML
        response = requests.get(youtube_url)
        response.raise_for_status()

        # Step 2: Find the JSON object with player data and parse it
        pattern = r"var ytInitialPlayerResponse = ({.*?});"
        match = re.search(pattern, response.text)

        if not match:
            print("Could not find player data in the HTML.")
            return None

        player_data = json.loads(match.group(1))
        print(player_data)
        
        # Step 3: Extract the URL of the first available subtitle track
        caption_tracks = player_data.get('captions', {}).get('playerCaptionsTracklistRenderer', {}).get('captionTracks', [])

        if not caption_tracks:
            print("No subtitle tracks available for this video.")
            return None

        subtitle_url = caption_tracks[0].get('baseUrl')
        if not subtitle_url:
            print("Could not find base URL for the first subtitle track.")
            return None

        # Step 4: Download the subtitle text (XML)
        subtitle_response = requests.get(subtitle_url)
        subtitle_response.raise_for_status()
        
        # Step 5: Parse the XML to extract just the text
        root = ET.fromstring(subtitle_response.text)
        full_text = []
        for text_element in root.findall('text'):
            full_text.append(text_element.text)
        
        return " ".join(full_text)

    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the request: {e}")
        return None
    except (json.JSONDecodeError, KeyError, ET.ParseError) as e:
        print(f"An error occurred while parsing the data: {e}")
        return None

# --- Example Usage ---
if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=Bg8_h6Bt1VI"  # Rick Astley's "Never Gonna Give You Up"
    subtitles = get_youtube_subtitles(video_url)

    if subtitles:
        print("\n--- Extracted Subtitle Text ---")
        print(subtitles)
    else:
        print("\nFailed to retrieve subtitles.")

