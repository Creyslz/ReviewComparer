import sys
import os.path
from amazon_search import ParseSearch
from custom_parser import ParseReviews
from phrase_processor import phrase_replace
from time import sleep

def compare_reviews_from_search(search_term):
  print(search_term)
  return
  results = ParseSearch(search_term)
  if len(results) == 0:
    return 'No results found'
  sleep(5)
  if len(results) < 5:
    return compare_reviews_from_list(results)
  return compare_reviews_from_list(results[:5])
  
def compare_reviews_from_list(asin_list):
  print(asin_list)
  queries = set()
  #with open corpus file
  for asin in asin_list:
    #load names
    if os.path.exists(asin + '_reviews_rated_1.txt'):
      #load from file
    else:
      reviews = ParseReviews(asin)
      #save to file
    #for star rating
    #do phrase replacement
    #remove newlines
    #grab unique words
    #save to corpus
  #save queries
  #do BM 25
  return
  
def main():
  # print command line arguments
  result = ''
  if sys.argv[1] == '-l':
    result = compare_reviews_from_list(sys.argv[2:])
  else:
    result = compare_reviews_from_search(sys.argv[1])
    

if __name__ == "__main__":
  main()