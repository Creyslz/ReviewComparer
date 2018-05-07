# ReviewComparer
To compare reviews on amazon using data mining.

Usage
Clone the repository and then run
python ReviewComparer.py "product search term"
eg
python ReviewComparer.py "laptop computer"
This will compare the top 4 results for the given search term.

or
python ReviewComparer.py asin1 asin2 asin3 ... (for an arbitrary number of asin's)
This will compare the products of the given asin's.

Asin stands for Amazon standard identification number
Asin's are 10 character codes that can be found in every amazon product url
                                                                        This part
                                                                        |        |    
https://www.amazon.com/Dell-OptiPlex-Processor-Certified-Refurbished/dp/B01AWOAUJY/

Some other examples are
B01AWOAUJY
B01CV9G1BO
B00IOTZGOE
B07BJMS28D


The expected output is of the form
generated using
python ReviewComparer.py "blender"

Results for Ninja Professional Blender (BL610):
5 star(s): ['sharp', 'yes', 'later', 'margarita', 'snow']
4 star(s): ['vita', 'finger', 'sharp', 'battl', 'compat']
3 star(s): ['chia', 'catch', 'five', 'tier', 'graini']
2 star(s): ['bp', 'ave', 'form', 'crack', 'worked_great']
1 star(s): ['zero', 'shelf', 'clip', 'crack', 'useless']
Results for Hamilton Beach (52400) Blender with 32 Oz Jar, For:
5 star(s): ['milkshak', 'mini', 'sleek', 'curri', 'fund']
4 star(s): ['bottl', 'switch', 'aspect', 'vendor', 'yoghurt']
3 star(s): ['bonus', 'suck', 'insecur', 'crevic', 'chopper']
2 star(s): ['luck', 'mason', 'weird', 'someone_ind', 'stinki']
1 star(s): ['smoke', 'wast', 'peach', 'fire', 'the_only_thing_it']
Results for Nutri Ninja Pro Blender, Silver (BL456):
5 star(s): ['recip', 'book', 'eat', 'common', 'pro']
4 star(s): ['overtighten', 'dirt', 'glitch', 'nutribullet', 'twist']
3 star(s): ['corrug', 'chainsaw', 'heck', 'planet', 'encount']
2 star(s): ['sharkninja', 'to_play', 'everyone_in', 'polici', 'pro']
1 star(s): ['dead', 'lousi', 'condit', 'spark', 'so_into']
Results for BLACK+DECKER Countertop Blender with 5-Cup Glass J:
5 star(s): ['works_great_and', 'very_pleased_with', 'great_valu', 'great_buy', 'surpass']
4 star(s): ['four_star', 'splater', 'ding', 'strongest', 'time_it']
3 star(s): ['macho', 'flake', 'smart', 'than_it', 'thing_in']
2 star(s): ['stall', 'dis', 'satisifi', 'ridg', 'i_tried_to']
1 star(s): ['deck', 'siev', 'er', 'disast', 'doesn_t_even']



Note that Amazon lacks an official API to grab their reviews so we get all of our reviews from scraping their website. This can take some time due to sleep statements that we have purposely placed between queries to amazon in order to prevent getting ratelimited by their website. We also limit the number of reviews we scrape for each product to the top 100 most useful as rated by amazon, but this can be changed by altering kLimitPages in ReviewComparer.py 

This output shows the kinds of words that best differentiate each product, rating pair from other product rating pairs.
Results are sorted by their BM25 scores where the queries are the words and the document is all of the reviews of the product, rating pair.


The phrases used by phrase_segmentation are generated from https://github.com/shangjingbo1226/AutoPhrase
Their code is applied to a corpus of all reviews that we have collected.

People who worked on this project
cshang4, jianing2, siqig2 (@illinois.edu)
Amazon scraping and phrase mining was done by cshang4.
Implementing BM25 and interpreting the results was done by jianing2 and siqig2.




