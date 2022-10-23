import nltk
from nltk.book import *
from nltk.corpus import stopwords

clean_tokens = []
for token in text1:
  if token not in stopwords.words('english'):
    clean_tokens.append(token)
 
freq1 = nltk.FreqDist(text1)
freq1.plot(20, cumulative=False)

freq2 = nltk.FreqDist(clean_tokens)
freq2.plot(20, cumulative=False)
