from lxml import html  
import json
import requests
import json,re
from dateutil import parser as dateparser
from time import sleep
import random
import pickle

# Input:
# asin, amazon product id
# limit_pages, limits the number of pages of reviews to load
# filter_by_rating, int representing the star rating of reviews to load
#                   0 or other nonesense values result in all reviews loading
# returns:
# list of concatenated reviews for each star rating
def ParseReviews(asin, limit_pages = 25, filter_by_rating = 0):
  stars = ['none', 'one_star', 'two_star', 'three_star', 'four_star', 'five_star']
  amazon_url_base  = 'http://www.amazon.com/product-reviews/' + asin + '/?filterByStar=' + stars[filter_by_rating] + '&pageNumber='
  output = {5:'', 4:'', 3:'', 2:'', 1:''}
  
  headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
  
  page_number = 1
  first = True
  reviews = 1
  #save names
  while reviews and page_number <= limit_pages:
    print('Getting page ' + str(page_number) + ' of a possible ' + str(limit_pages) + '.')
    amazon_url = amazon_url_base + str(page_number)
    page_number += 1
    page = requests.get(amazon_url,headers = headers,verify=False)
    sleep(5. + random.random()) # Sleep between requests so Amazon doesn't ban me
    page_response = page.text

    parser = html.fromstring(page_response)
    XPATH_REVIEW_SECTION = '//div[@data-hook="review"]'
    
    reviews = parser.xpath(XPATH_REVIEW_SECTION)
    #print(reviews)
    for review in reviews:
      XPATH_RATING  = './/i[@data-hook="review-star-rating"]//text()'
      XPATH_REVIEW_HEADER = './/a[@data-hook="review-title"]//text()'
      XPATH_REVIEW_TEXT  = './/span[@data-hook="review-body"]//text()'
      
      raw_review_rating = review.xpath(XPATH_RATING)
      raw_review_header = review.xpath(XPATH_REVIEW_HEADER)
      raw_review_text = review.xpath(XPATH_REVIEW_TEXT)
      
      review_rating = int((''.join(raw_review_rating).replace('out of 5 stars',''))[0])
      review_header = ' '.join(' '.join(raw_review_header).split())
      
      review_text = ' '.join(' '.join(raw_review_text).split())
      output[review_rating] += review_header + '\n' + review_text + '\n'
  return output
  
def ReadAsin():
  #Add your own ASINs here 
  AsinList = ['B01AWOAUJY', 'B01CV9G1BO', 'B00IOTZGOE', 'B07BJMS28D']
  extracted_data = dict()
  for asin in AsinList:
    print("Downloading and processing page http://www.amazon.com/dp/"+asin)
    reviews = ParseReviews(asin)
    extracted_data[asin] = reviews
  pickle.dump(extracted_data, open('reviews.p', 'wb'))
  

if __name__ == '__main__':
  ReadAsin()