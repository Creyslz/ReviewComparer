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
def ParseSearch(searchTerm):
  amazon_url_base  = 'https://www.amazon.com/s/&field-keywords=' + searchTerm
  output = []
  
  headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
  
  sleep(5. + random.random())
  amazon_url = amazon_url_base
  page = requests.get(amazon_url,headers = headers,verify=False)
  page_response = page.text

  parser = html.fromstring(page_response)
  XPATH_RESULTS_SECTION = '//li[@class="s-result-item celwidget  "]'
  
  results = parser.xpath(XPATH_RESULTS_SECTION)
  #print(reviews)
  for asin in results:
    asin = asin.xpath('@data-asin')
    name = asin.xpath('.//h2[@class="a-size-medium s-inline  s-access-title  a-text-normal"]//text()')
  output.append(asin)
  return output
  
def amazonSearch():
  #Add your own ASINs here 
  searchList = ['laptop']
  first = True
  for term in searchList:
    print("Downloading and processing page https://www.amazon.com/s/&field-keywords="+term)
    reviews = ParseSearch(term)
    if first:
      first = False
    else:
      sleep(5. + random.random())
  

if __name__ == '__main__':
  amazonSearch()