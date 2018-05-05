import sys
import os.path
import review_to_text
from amazon_search import ParseSearch
from custom_parser import ParseReviews
from phrase_processor import phrase_replace
from time import sleep
import urllib3
from search_eval import process

is_debug = False

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
  queries = set()
  corpus_path = 'comparison_data/comparison_data.dat'
  if is_debug: corpus_path = 'comparison_data/comparison_data_t.dat'
  with open(corpus_path, 'w') as corpus:
    for asin in asin_list:
      print('Loading reviews for ' + str(asin) + '. This can take up to three minutes.')
      #load names
      corpus_line = ''
      if os.path.exists(asin + '_reviews_rated_1.txt'):
        reviews = review_to_text.load_all_reviews(asin)
      else:
        reviews = ParseReviews(asin, limit_pages = 5)
        reviews = review_to_text.clean_all_strings(reviews)
        review_to_text.save_all_reviews(asin, reviews)
      for star_rating, review in reviews.items():
        new_line = phrase_replace(review)
        if '\n' in new_line:
          print('new lines found')
          new_line = new_line.replace('\n', ' ')
      for word in new_line.split():
        queries.add(word)
      corpus.write(new_line + '\n')
  with open('comparison_data/queries.txt', 'w') as f:
    for word in queries:
      f.write(word + '\n')
  process(5)
  return
  
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