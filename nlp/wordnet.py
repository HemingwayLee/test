from nltk.corpus import wordnet
 
ss = wordnet.synsets("pain")
print(ss[0].definition())
print(ss[0].examples())


synonyms = [] 
for syn in wordnet.synsets('huge'):
  for lemma in syn.lemmas():
    synonyms.append(lemma.name())

print(synonyms)

 
antonyms = []
for syn in wordnet.synsets("small"):
  for l in syn.lemmas():
    if l.antonyms():
      antonyms.append(l.antonyms()[0].name())
 
print(antonyms)