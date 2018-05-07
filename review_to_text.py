import pickle
import string

# This file is a bunch of helper functions handling reviews and cacheing

# saves the reviews of a single product, star rating pair
def save_reviews(asin, stars, reviews):
  path = 'reviews/'
  file_name_base = '_reviews_rated_'
  with open(path + asin + file_name_base + str(stars) + '.txt', 'w') as f:
    f.write(reviews)

# saves all the reviews of a product
# the reviews for each star rating are saved in a seperate file
def save_all_reviews(asin, reviews):
  #print(reviews)
  for stars in range(1,6):
    save_reviews(asin, stars, reviews[stars])

# loads the reviews for a single asin star rating pair
# returns all the reviews as a single string
def load_reviews(asin, stars):
  path = 'reviews/'
  file_name_base = '_reviews_rated_'
  output = []
  with open(path + asin + file_name_base + str(stars) + '.txt', 'r') as f:
    output = f.readlines()
  return ' '.join(output)

# loads all the reviews for a given asin
# returns the reveiws as a dictionary with the star rating as the key
def load_all_reviews(asin):
  output = dict()
  for stars in range(1,6):
    output[stars] = load_reviews(asin, stars)
  return output
  
# gets the set of unique words from a string
def get_unique_words(string):
  output = set()
  for word in string.split():
    output.add(word)
  return output

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

# removes capitalization, punctuation and reencodes as ascii
# saves so future lookups don't have to query amazon
# input is a dictionary where the values are the strings that need to be cleaned
# returns the cleaned dictionary
def clean_all_strings(review_dict):
  output = dict()
  for star_rating, review in review_dict.items():
    line = review.encode('ascii','ignore').decode("ascii")
    line = line.lower()
    translator = str.maketrans(string.punctuation, ' '*len(string.punctuation))
    line = line.translate(translator)
    output[star_rating] = line
  return output
  
  

if __name__ == '__main__':
  raw_reviews = pickle.load(open('reviews1.p', 'rb'))

  path = 'reviews/'
  file_name_base = '_reviews_rated_'
  all_words = set()
  lines = [[],[],[],[],[]]
  current_line = []
  output_lines = []
  for product, product_reviews in raw_reviews.items():
    for star_rating, review in product_reviews.items():
      current_line = []
      with open(path + product + file_name_base + str(star_rating) + '.txt', 'w') as f:
        line = review.encode('ascii','ignore').decode("ascii")
        line = line.lower()
        translator = str.maketrans(string.punctuation, ' '*len(string.punctuation))
        line = line.translate(translator)
        f.write(line)
        current_line=line.strip()
        current_line = current_line.replace('\n','')
        for word in line.split():
          all_words.add(word)
        lines[star_rating-1].append(current_line)
    for line in lines:
      clean = [s.replace('\n', '') for s in line]
      if '\n' in clean: print(clean)
      output_lines.append(''.join(clean))
      print(len(output_lines))
  with open('comparison_data/corpus.dat', 'w') as fout:
    for line in output_lines:
      fout.write( ''.join(line) + '\n')
  with open('comparison_data/queries.txt', 'w') as f:
    for word in all_words:
      f.write(word + '\n')
  #print(all_words)
  print(len(all_words))