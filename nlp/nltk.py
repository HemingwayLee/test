import nltk
from nltk.book import *

# it will show a popup UI to download 
# nltk.download()

fd1 = FreqDist(text1)
print(fd1.most_common(20))

fd2 = FreqDist(text2)
print(fd2.most_common(20))

fd1.plot(20, cumulative=False)