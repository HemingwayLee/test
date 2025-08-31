from pytube import YouTube
from pytube.exceptions import PytubeError
import xml.etree.ElementTree as ET

def get_subtitles_with_pytube(youtube_url, lang_code='en'):
    """
    Fetches the subtitle text for a specific language using pytube.
    
    Args:
        youtube_url (str): The full URL of the YouTube video.
        lang_code (str): The two-letter language code for the desired subtitles.
    
    Returns:
        str or None: The parsed subtitle text, or None on failure.
    """
    try:
        yt = YouTube(youtube_url)
        
        # Get the first available caption track
        # You can specify a language code here, e.g., yt.captions.get_by_language_code('zh-TW')
        caption = next(iter(yt.captions.values()), None)

        if not caption:
            print("No subtitles found for this video.")
            return None
        
        # Download the subtitle content in XML format
        xml_content = caption.xml_captions

        # Parse the XML to extract just the text
        root = ET.fromstring(xml_content)
        full_text = [element.text for element in root.findall('text')]
        
        return " ".join(full_text)

    except PytubeError as e:
        print(f"A Pytube error occurred: {e}")
        return None
    except ET.ParseError as e:
        print(f"XML parsing error: {e}")
        return None

# Example Usage
if __name__ == "__main__":
    # URL of a video with subtitles in zh-TW
    video_url = "https://www.youtube.com/watch?v=Bg8_h6Bt1VI"
    subtitles = get_subtitles_with_pytube(video_url)

    if subtitles:
        print("\n--- Extracted Subtitle Text ---")
        print(subtitles)
    else:
        print("\nFailed to retrieve subtitles.")

