import pickle

phrases = set()

with open('AutoPhrase_multi-words.txt', 'r') as text:
  for line in text.readlines():
    segs = line[:-1].split('\t')
    phrases.add(segs[1])

pickle.dump(phrases, open('phrases.p', 'wb'))