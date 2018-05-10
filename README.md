# ReviewComparer
To compare reviews on amazon using data mining.

Usage
Clone the repository and then run
```
python ReviewComparer.py "product search term"
```
eg
```
python ReviewComparer.py "laptop computer"
```
This will compare the top 4 results for the given search term.

or
```
python ReviewComparer.py -l ASIN1 ASIN2 ASIN3 ... (for an arbitrary number of ASIN's)
```
This will compare the products of the given ASIN's.

ASIN stands for Amazon Standard Identification Number.
ASIN's are 10 character codes that can be found in every Amazon product url
```
                                                                        This part
                                                                        |        |    
https://www.amazon.com/Dell-OptiPlex-Processor-Certified-Refurbished/dp/B01AWOAUJY/
```

Some other examples are
```
B01AWOAUJY
B01CV9G1BO
B00IOTZGOE
B07BJMS28D
```

Example output
```
python ReviewComparer.py "blender"
```
```
Results for Ninja Professional Blender (BL610):
5 star(s): ['sharp', 'up_to_th', 'yes', 'margarita', 'later']
4 star(s): ['vita', 'finger', 'reli', 'battl', 'minc']
3 star(s): ['buy_it_again', 'chia', 'catch', 'but_i_wouldn_t', 'graini']
2 star(s): ['bp', 'because_i_h', 'have_to_do_that', 'worked_great', 'ave']
1 star(s): ['let_m', 'shelf', 'clip', 'blender_i_have_ev', 'blender_for_what_you_pay']
Results for Hamilton Beach (52400) Blender with 32 Oz Jar, For:
5 star(s): ['me_and', 'milkshak', 'mini', 'sleek', 'is_awesom']
4 star(s): ['bottl', 'while_it', 'while_it_', 'switch', 'shred']
3 star(s): ['with_this_item', 'however_the_blad', 'bonus', 'not_veri', 'suck']
2 star(s): ['i_m_sure_it_', 'not_very_happy_with_thi', 'blender_for_about_3_month', 'luck', 'this_was_a_great_littl']
1 star(s): ['not_recommend', 'smoke', 'about_the_only_thing_it_is_good_for', 'that_someday_i_wil', 'and_got']
Results for Nutri Ninja Pro Blender, Silver (BL456):
5 star(s): ['recip', 'book', 'eat', 'drive', 'love_it_']
4 star(s): ['the_bullet', 'overtighten', 'give_this_product', 'glitch', 'frozen_fruits_and_it_shr']
3 star(s): ['corrug', 'chainsaw', 'heck', 'encount', 'have_yet_to']
2 star(s): ['sharkninja', 'the_unit', 'and_now_i_have_to_play', 'i_mad', 'i_purchased_this_item']
1 star(s): ['dead', 'lousi', 'but_the_motor', 'condit', 'spark']
Results for BLACK+DECKER Countertop Blender with 5-Cup Glass J:
5 star(s): ['i_got_it_for_mi', 'every_day_and_it_s_stil', 'dad', 'and_i_dont', 'crank']
4 star(s): ['four_star', 'exactly_what_i_thought', 'great_but_it', 'i_like_the_best', 'great_blender_for_the_money']
3 star(s): ['not_as_good_as_a', 'of_their', 'macho', 'you_have_to_be_veri', 'while_it_do']
2 star(s): ['that_it_does_not', 'caus', 'on_the_blend', 'do_a_very_good_job', 'languag']
1 star(s): ['was_not', 'deck', 'siev', 'of_them', 'brand_and_th']
```

# search_eval
Implemented with BM25 method imported from Metapy, Search-eval provides a list of top five words(queries) with highest ranking scores corresponding to each corpus, incorporating with stop-words removal and stemming filter to avoid common words, numbers and words with same roots. The third argument is the number of words you hope to get for each review corpus.

Usage
```
python search_eval.py word_num
```
Example 1
```
python search_eval.py 5
```
```
[['vitamix', 'food', 'pulver', 'lock', 'blade'], ['vita', 'heat', 'dull', 'fiber', 'sharp'], None, None, ['clip', 'broken', 'broke', 'warranti', 'explod'], ['18oz', '24oz', 'oz', '32oz', '16oz'], ['attach', 'small', 'milk', 'aspect', 'touch'], None, ['weird', 'fli', 'burnt', 'usual', 'explod'], ['ad', 'turn', 'move', 'got', 'if_it'], ['seal', 'common', 'recip', 'pro', 'nutri'], ['dirt', 'hi', 'ur', 'cool', 'fabric'], ['packag', 'corrug', 'box', 'amazon', 'planet'], ['the_unit', 'unit', 'to_se', 'abil', 'strip'], ['plan', 'rubber', 'smell', 'nutri', '2nd'], ['great_valu', 'thick', 'loosen', 'slip', 'ici'], ['consist', 'shake', 'ding', 'time_it', 'coconut'], ['macho', 'expect', 'tool', 'loud', 'cheap'], None, ['applianc', 'die', 'the_box', 'proper', ‘dollar']]
```
Example 2
```
python search_eval.py 10
```
```
[['vitamix', 'food', 'pulver', 'lock', 'blade', 'click', 'pour', 'ninja', 'cleanli', 'clean'], ['vita', 'heat', 'dull', 'fiber', 'sharp', 'notic', 'veggi', 'reli', 'appl', 'comparison'], None, None, ['clip', 'broken', 'broke', 'warranti', 'explod', 'defect', 'pay', 'state', 'usag', 'lock'], ['18oz', '24oz', 'oz', '32oz', '16oz', 'shake', 'kid', 'milkshak', 'fashion', 'opportun'], ['attach', 'small', 'milk', 'aspect', 'touch', 'lot', 'option', 'switch', 'power', 'ingredi'], None, ['weird', 'fli', 'burnt', 'usual', 'explod', 'smoke', 'a_month', 'start', 'morn', 'piec'], ['ad', 'turn', 'move', 'got', 'if_it', 'back', 'the_first', 'wast', 'middl', 'mother'], ['seal', 'common', 'recip', 'pro', 'nutri', 'almond', 'review', 'this_product', 'fill', 'good'], ['dirt', 'hi', 'ur', 'cool', 'fabric', 'explain', 'mark', 'black', 'came', 'color'], ['packag', 'corrug', 'box', 'amazon', 'planet', 'shop', 'less_than_idea', 'seven', 'larger', 'able_to_mak'], ['the_unit', 'unit', 'to_se', 'abil', 'strip', 'did_not', 'told', 'was_not', 'sale', 'unfortun'], ['plan', 'rubber', 'smell', 'nutri', '2nd', 'protect', 'fool', 'manufactur', 'the_compani', 'serial'], ['great_valu', 'thick', 'loosen', 'slip', 'ici', 'strength', 'to_settl', 'whirlpool', 'the_qual', 'gear'], ['consist', 'shake', 'ding', 'time_it', 'coconut', 'delici', 'scrub', 'handl', 'hundr', 'strongest'], ['macho', 'expect', 'tool', 'loud', 'cheap', 'leak', 'basic', 'job', 'super', 'bueno'], None, ['applianc', 'die', 'the_box', 'proper', 'dollar', 'arriv', 'understat', 'dishrag', 'quit', ‘cream']]
```
#
Note that Amazon lacks an official API to grab their reviews so we get all of our reviews from scraping their website. This can take some time due to sleep statements that we have purposely placed between queries to amazon in order to prevent getting ratelimited by their website. We also limit the number of reviews we scrape for each product to the top 100 most useful as rated by amazon, but this can be changed by altering kLimitPages in ReviewComparer.py 

This output shows the kinds of words that best differentiate each product, rating pair from other product rating pairs.
Results are sorted by their BM25 scores where the queries are the words and the document is all of the reviews of the product, rating pair.

The phrases used by phrase_segmentation are generated from https://github.com/shangjingbo1226/AutoPhrase
Their code is applied to a corpus of all reviews that we have collected.

People who worked on this project

cshang4, jianing2, siqig2 (@illinois.edu)

Amazon scraping and phrase mining was done by cshang4.

Implementing BM25 and interpreting the results was done by jianing2 and siqig2.

