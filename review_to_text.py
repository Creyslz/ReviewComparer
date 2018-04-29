import pickle
import string

# removes capitalization, punctuation and reencodes as ascii
# saves so future lookups don't have to query amazon
# returns the cleaned review
def save_reviews(asin, stars, reviews):
  path = 'reviews/'
  file_name_base = '_reviews_rated_'
  with open(path + asin + file_name_base + str(stars) + '.txt', 'w') as f:
    line = review.encode('ascii','ignore').decode("ascii")
    line = line.lower()
    translator = str.maketrans(string.punctuation, ' '*len(string.punctuation))
    line = line.translate(translator)
    f.write(line)
  return line

def load_reviews(asin, stars):
  path = 'reviews/'
  file_name_base = '_reviews_rated_'
  output = []
  with open(path + asin + file_name_base + str(stars) + '.txt', 'r') as f:
    output = f.readlines()
  return ' '.join(output)

def get_unique_words(string):
  output = set()
  for word in string.split():
    output.add(word)
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