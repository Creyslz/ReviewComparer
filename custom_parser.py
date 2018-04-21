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
# returns:
# list of concatenated reviews for each star rating
def ParseReviews(asin):
  amazon_url_base  = 'http://www.amazon.com/product-reviews/' + asin + '/?pageNumber='
  output = {5:'', 4:'', 3:'', 2:'', 1:''}
  
  headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
  
  page_number = 1
  first = True
  reviews = 1
  while reviews:
    if first:
      first = False
    else:
      sleep(5. + random.random())
    amazon_url = amazon_url_base + str(page_number)
    page_number += 1
    page = requests.get(amazon_url,headers = headers,verify=False)
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
  AsinList = ['B01AWOAUJY']
  extracted_data = {5:'', 4:'', 3:'', 2:'', 1:''}
  first = True
  for asin in AsinList:
    print("Downloading and processing page http://www.amazon.com/dp/"+asin)
    reviews = ParseReviews(asin)
    for i in range(1,6):
      extracted_data[i] += reviews[i]
    if first:
      first = False
    else:
      sleep(5. + random.random())
  pickle.dump(extracted_data, open('reviews.p', 'wb'))
  print(extracted_data)
  

if __name__ == '__main__':
  ReadAsin()