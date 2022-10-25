from youtube_transcript_api import YouTubeTranscriptApi

transcript_list = YouTubeTranscriptApi.list_transcripts("dfd9H2Xtz0A")
# print(transcript_list)

# transcript = transcript_list.find_transcript(['ja', 'en'])
# print(transcript)

# transcript = transcript_list.find_generated_transcript(['ja', 'en'])
# print(transcript)

res = YouTubeTranscriptApi.get_transcript("dfd9H2Xtz0A", languages=['ja'])
# print(res)

total = ""
for ele in res:
    # print(ele)
    total += ele["text"]

print(total)
print(f'total sec: {res[-1]["start"] + res[-1]["duration"]}')
print(f'total words: {len(total)}')
print(f'money: {0.4 * len(total)}')
print(f'money: {1.2 * len(total)}')


