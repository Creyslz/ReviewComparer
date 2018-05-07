import pickle
import string

# Converts the list of multi-word phrases returned by autophrase 
# into a set that is pickled for easy access


# removes capitalization, punctuation and reencodes as ascii
# saves so future lookups don't have to query amazon
# input is a single string
# returns the cleaned review  
def clean_string(in_string):
  line = in_string.encode('ascii','ignore').decode("ascii")
  line = line.lower()
  translator = str.maketrans(string.punctuation, ' '*len(string.punctuation))
  line = line.translate(translator)
  return line

phrases = set()

with open('AutoPhrase_multi-words.txt', 'r') as text:
  for line in text.readlines():
    segs = line[:-1].split('\t')
    nstring = clean_string(segs[1])
    if len(nstring) > 3:
      phrases.add(segs[1])

pickle.dump(phrases, open('phrases.p', 'wb'))