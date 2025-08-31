from youtube_transcript_api import YouTubeTranscriptApi

ytt_api = YouTubeTranscriptApi()

fetched_transcript = ytt_api.fetch("Bg8_h6Bt1VI", languages=['zh-TW'])

# is iterable
for snippet in fetched_transcript:
    print(snippet.text)

# indexable
last_snippet = fetched_transcript[-1]

# provides a length
snippet_count = len(fetched_transcript)


