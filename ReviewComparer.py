import sys
import os.path
import review_to_text
from amazon_search import ParseSearch
from custom_parser import ParseReviews
from phrase_processor import phrase_replace
from time import sleep
import urllib3
from search_eval import process
import pickle
import math

is_debug = False
kLimitPages = 10

# 
def compare_reviews_from_search(search_term):
  results = ParseSearch(search_term)
  if len(results) == 0:
    return 'No results found'
  sleep(5)
  if len(results) < 4:
    return compare_reviews_from_list(results)
  return compare_reviews_from_list(results[:4])
  
def compare_reviews_from_list(asin_list):
  print(asin_list)

  asin_name = pickle.load(open('reviews/asin_name_dict.p', 'rb'))
  #print(asin_name)
  names = []
  star_ratings = []
  queries = set()
  corpus_path = 'comparison_data/comparison_data.dat'
  with open(corpus_path, 'w') as corpus:
    for asin in asin_list:
      max_time = str(math.ceil((kLimitPages + 1.)*5./60.))
      print('Loading reviews for '+str(asin)+'. This can take up to '+max_time+' minute(s).')
      corpus_line = ''
      name = asin
      if asin in asin_name:
        name = asin_name[asin]
      if not is_debug and os.path.exists('reviews/' + asin + '_reviews_rated_1.txt'):
        reviews = review_to_text.load_all_reviews(asin)
      else:
        reviews = ParseReviews(asin, limit_pages = kLimitPages)
        reviews = review_to_text.clean_all_strings(reviews)
        review_to_text.save_all_reviews(asin, reviews)
      for star_rating in range(5,0,-1):
        review = reviews[star_rating]
        names.append(name[:min(len(name), 50)])
        star_ratings.append(str(star_rating))
        new_line = phrase_replace(review)
        if '\n' in new_line:
          new_line = new_line.replace('\n', ' ')
        for word in new_line.split():
          queries.add(word)
        corpus.write(new_line + '\n')
  with open('queries.txt', 'w') as f:
    for word in queries:
      f.write(word + '\n')
  results = process(len(asin_list) * 5)
  #print(results)
  i = 0
  for row in results:
    if i%5 == 0:
      print('Results for ' + names[i] + ':')
    if row:
      print(star_ratings[i] + ' star(s):', row)
    else:
      print(star_ratings[i] + ' star(s): No reviews found.')
    i += 1
  return results
  
def main():
  # print command line arguments
  result = ''
  urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
  if sys.argv[1] == '-l':
    result = compare_reviews_from_list(sys.argv[2:])
  else:
    result = compare_reviews_from_search(sys.argv[1])
    

if __name__ == "__main__":
  main()