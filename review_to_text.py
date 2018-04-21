import pickle
import string

reviews = pickle.load(open('reviews.p', 'rb'))

file_name_base = 'review_docs/reviews_rated_'
all_words = set()
for i in range(1,6):
  with open(file_name_base + str(i) + '.txt', 'w') as f:
    line = reviews[i].encode('ascii','ignore').decode("ascii")
    line = line.lower()
    translator = str.maketrans(string.punctuation, ' '*len(string.punctuation))
    line = line.translate(translator)
    f.write(line)
    for word in line.split():
      all_words.add(word)
print(all_words)
print(len(all_words))