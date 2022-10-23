import nltk


sentence = """At eight o'clock on Thursday morning, Arthur didn't feel very good."""
tokens = nltk.word_tokenize(sentence)
tagged = nltk.pos_tag(tokens)
print(tagged)

# https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html