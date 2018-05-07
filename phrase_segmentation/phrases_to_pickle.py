import pickle

# Converts the list of multi-word phrases returned by autophrase 
# into a set that is pickled for easy access

phrases = set()

with open('AutoPhrase_multi-words.txt', 'r') as text:
  for line in text.readlines():
    segs = line[:-1].split('\t')
    phrases.add(segs[1])

pickle.dump(phrases, open('phrases.p', 'wb'))