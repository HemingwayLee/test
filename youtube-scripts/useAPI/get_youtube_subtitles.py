#!/usr/bin/env python3
"""
YouTube Subtitle Extractor using YouTube Data API v3

This script extracts subtitles/captions from YouTube videos using the YouTube Data API v3.
It can download both auto-generated and manually created captions in various formats.
"""

import os
import sys
import json
import argparse
from typing import List, Dict, Optional
from urllib.parse import urlparse, parse_qs

try:
    from googleapiclient.discovery import build
    from googleapiclient.errors import HttpError
except ImportError:
    print("Error: google-api-python-client is required. Install with:")
    print("pip install google-api-python-client")
    sys.exit(1)

class YouTubeSubtitleExtractor:
    def __init__(self, api_key: str):
        """Initialize the extractor with YouTube API key."""
        self.api_key = api_key
        self.youtube = build('youtube', 'v3', developerKey=api_key)
    
    def extract_video_id(self, url_or_id: str) -> str:
        """Extract video ID from YouTube URL or return ID if already provided."""
        if len(url_or_id) == 11 and url_or_id.isalnum():
            return url_or_id
        
        parsed_url = urlparse(url_or_id)
        if parsed_url.hostname in ['www.youtube.com', 'youtube.com']:
            if parsed_url.path == '/watch':
                return parse_qs(parsed_url.query)['v'][0]
            elif parsed_url.path.startswith('/embed/'):
                return parsed_url.path.split('/')[2]
        elif parsed_url.hostname == 'youtu.be':
            return parsed_url.path[1:]
        
        raise ValueError(f"Invalid YouTube URL or video ID: {url_or_id}")
    
    def get_video_info(self, video_id: str) -> Dict:
        """Get basic video information."""
        try:
            response = self.youtube.videos().list(
                part='snippet',
                id=video_id
            ).execute()
            
            if not response['items']:
                raise ValueError(f"Video not found: {video_id}")
            
            return response['items'][0]['snippet']
        except HttpError as e:
            raise Exception(f"API error getting video info: {e}")
    
    def get_available_captions(self, video_id: str) -> List[Dict]:
        """Get list of available caption tracks for a video."""
        try:
            response = self.youtube.captions().list(
                part='snippet',
                videoId=video_id
            ).execute()
            
            return response.get('items', [])
        except HttpError as e:
            raise Exception(f"API error getting captions: {e}")
    
    def download_caption(self, caption_id: str, format_type: str = 'srt') -> str:
        """Download caption content in specified format."""
        try:
            response = self.youtube.captions().download(
                id=caption_id,
                tfmt=format_type
            ).execute()
            
            return response.decode('utf-8')
        except HttpError as e:
            if e.resp.status == 403:
                raise Exception("Caption download forbidden. The video owner may have disabled caption downloads.")
            raise Exception(f"API error downloading caption: {e}")
    
    def get_subtitles(self, url_or_id: str, language: Optional[str] = None, 
                     format_type: str = 'srt', output_file: Optional[str] = None) -> str:
        """
        Main method to get subtitles from a YouTube video.
        
        Args:
            url_or_id: YouTube URL or video ID
            language: Language code (e.g., 'en', 'es', 'fr'). If None, uses first available
            format_type: Caption format ('srt', 'vtt', 'ttml')
            output_file: Optional file path to save subtitles
        
        Returns:
            Subtitle content as string
        """
        video_id = self.extract_video_id(url_or_id)
        
        # Get video info
        video_info = self.get_video_info(video_id)
        print(f"Video: {video_info['title']}")
        print(f"Channel: {video_info['channelTitle']}")
        
        # Get available captions
        captions = self.get_available_captions(video_id)
        
        if not captions:
            raise Exception("No captions available for this video")
        
        # Display available captions
        print(f"\nAvailable captions:")
        for i, caption in enumerate(captions):
            snippet = caption['snippet']
            track_kind = snippet.get('trackKind', 'standard')
            is_auto = track_kind == 'ASR'
            print(f"  {i+1}. {snippet['language']} ({snippet['name']}) {'[Auto-generated]' if is_auto else '[Manual]'}")
        
        # Select caption track
        selected_caption = None
        if language:
            for caption in captions:
                if caption['snippet']['language'] == language:
                    selected_caption = caption
                    break
            if not selected_caption:
                raise Exception(f"Caption language '{language}' not available")
        else:
            selected_caption = captions[0]  # Use first available
        
        print(f"\nUsing caption: {selected_caption['snippet']['language']} ({selected_caption['snippet']['name']})")
        
        # Download caption
        caption_content = self.download_caption(selected_caption['id'], format_type)
        
        # Save to file if specified
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(caption_content)
            print(f"Subtitles saved to: {output_file}")
        
        return caption_content

def main():
    parser = argparse.ArgumentParser(description="Extract subtitles from YouTube videos using API v3")
    parser.add_argument('video', help='YouTube URL or video ID')
    parser.add_argument('--api-key', required=True, help='YouTube Data API v3 key')
    parser.add_argument('--language', help='Language code (e.g., en, es, fr)')
    parser.add_argument('--format', choices=['srt', 'vtt', 'ttml'], default='srt', 
                       help='Subtitle format (default: srt)')
    parser.add_argument('--output', help='Output file path')
    parser.add_argument('--list-only', action='store_true', 
                       help='Only list available captions, don\'t download')
    
    args = parser.parse_args()
    
    try:
        extractor = YouTubeSubtitleExtractor(args.api_key)
        
        if args.list_only:
            video_id = extractor.extract_video_id(args.video)
            video_info = extractor.get_video_info(video_id)
            captions = extractor.get_available_captions(video_id)
            
            print(f"Video: {video_info['title']}")
            print(f"Available captions:")
            for caption in captions:
                snippet = caption['snippet']
                track_kind = snippet.get('trackKind', 'standard')
                is_auto = track_kind == 'ASR'
                print(f"  - {snippet['language']} ({snippet['name']}) {'[Auto-generated]' if is_auto else '[Manual]'}")
        else:
            content = extractor.get_subtitles(
                args.video, 
                language=args.language,
                format_type=args.format,
                output_file=args.output
            )
            
            if not args.output:
                print("\n--- Subtitle Content ---")
                print(content)
    
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()