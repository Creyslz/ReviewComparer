import pickle
import string

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
    if len(output_lines) == 3: print(clean)
    output_lines.append(''.join(clean) + '\n')
    print(len(output_lines))
with open('comparison_data/corpus.txt', 'w') as fout:
  for line in lines:
    fout.write( ''.join(output_lines) + '\n')
with open('comparison_data/queries.txt', 'w') as f:
  for word in all_words:
    f.write(word + '\n')
#print(all_words)
print(len(all_words))