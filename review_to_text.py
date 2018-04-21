import pickle
import string

raw_reviews = pickle.load(open('reviews1.p', 'rb'))

path = 'reviews/'
file_name_base = '_reviews_rated_'
all_words = set()
for product, product_reviews in raw_reviews.items():
  for star_rating, review in product_reviews.items():
    with open(path + product + file_name_base + str(star_rating) + '.txt', 'w') as f:
      line = review.encode('ascii','ignore').decode("ascii")
      line = line.lower()
      translator = str.maketrans(string.punctuation, ' '*len(string.punctuation))
      line = line.translate(translator)
      f.write(line)
      for word in line.split():
        all_words.add(word)
print(all_words)
print(len(all_words))