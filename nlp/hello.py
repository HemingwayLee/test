import requests

with open('litecoin_bad.txt', 'r') as myfile:
  mytxt=myfile.read().replace('\n', '')

print(mytxt)

r = requests.post(
  "http://text-processing.com/api/sentiment/", 
  data={'text': mytxt}
)

print(r.status_code, r.reason)
print(r.text)

# http://text-processing.com/docs/sentiment.html