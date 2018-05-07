from lxml import html  
import json
import requests
import json,re
from time import sleep
import random
import pickle

# Input:
# A search term
# returns:
# list of asin's 
# This function also updates the asin, product name dictionary
def ParseSearch(searchTerm):
  try:
    asin_name_dict = pickle.load(open('reviews/asin_name_dict.p', 'rb'))
  except:
    asin_name_dict = dict()


  amazon_url_base  = 'https://www.amazon.com/s/&field-keywords=' + searchTerm
  output = []
  
  headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
  
  amazon_url = amazon_url_base
  page = requests.get(amazon_url,headers = headers,verify=False)
  print('Getting search results for ' + searchTerm + '.')
  sleep(5. + random.random()*.5)
  page_response = page.text

  parser = html.fromstring(page_response)
  XPATH_RESULTS_SECTION = '//li[@class="s-result-item celwidget  "]'
  
  results = parser.xpath(XPATH_RESULTS_SECTION)
  #print(reviews)
  for asin_s in results:
    asin = asin_s.xpath('@data-asin')
    name = asin_s.xpath('.//h2[@class="a-size-medium s-inline  s-access-title  a-text-normal"]//text()')
    #print(asin, name)
    if asin and name:
      output.append(asin[0])
      if asin[0] not in asin_name_dict:
        asin_name_dict[asin[0]] = name[0]
  pickle.dump(asin_name_dict, open('reviews/asin_name_dict.p', 'wb'))
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