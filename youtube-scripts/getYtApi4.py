import requests
import re
import json
import xml.etree.ElementTree as ET

def get_youtube_subtitles(youtube_url):
    try:
        response = requests.get(youtube_url)
        response.raise_for_status()

        pattern = r"var ytInitialPlayerResponse = ({.*?});"
        match = re.search(pattern, response.text)

        if not match:
            print("Could not find player data in the HTML.")
            return None

        player_data = json.loads(match.group(1))
        
        caption_tracks = player_data.get('captions', {}).get('playerCaptionsTracklistRenderer', {}).get('captionTracks', [])

        if not caption_tracks:
            print("No subtitle tracks available for this video.")
            return None

        subtitle_url = caption_tracks[0].get('baseUrl')
        
        print(f"subtitle url is {subtitle_url}")
        
        if not subtitle_url:
            print("Could not find base URL for the first subtitle track.")
            return None

        # Download the subtitle text (XML)
        subtitle_response = requests.get(subtitle_url)
        subtitle_response.raise_for_status()

        print(subtitle_response.text)

        # Check if the subtitle text is empty before parsing
        if not subtitle_response.text.strip():
            print("Subtitle content is empty. The track may not have subtitles.")
            return None
        
        # Parse the XML to extract just the text
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

# Example Usage
if __name__ == "__main__":
    # URL of a video with known subtitles
    video_url = "https://www.youtube.com/watch?v=Bg8_h6Bt1VI"
    subtitles = get_youtube_subtitles(video_url)

    if subtitles:
        print("\n--- Extracted Subtitle Text ---")
        print(subtitles)
    else:
        print("\nFailed to retrieve subtitles.")


