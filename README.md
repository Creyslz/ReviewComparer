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
python ReviewComparer.py asin1 asin2 asin3 ... (for an arbitrary number of asin's)
```
This will compare the products of the given asin's.

Asin stands for Amazon standard identification number.
Asin's are 10 character codes that can be found in every amazon product url
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


Note that Amazon lacks an official API to grab their reviews so we get all of our reviews from scraping their website. This can take some time due to sleep statements that we have purposely placed between queries to amazon in order to prevent getting ratelimited by their website. We also limit the number of reviews we scrape for each product to the top 100 most useful as rated by amazon, but this can be changed by altering kLimitPages in ReviewComparer.py 

This output shows the kinds of words that best differentiate each product, rating pair from other product rating pairs.
Results are sorted by their BM25 scores where the queries are the words and the document is all of the reviews of the product, rating pair.

The phrases used by phrase_segmentation are generated from https://github.com/shangjingbo1226/AutoPhrase
Their code is applied to a corpus of all reviews that we have collected.

People who worked on this project

cshang4, jianing2, siqig2 (@illinois.edu)

Amazon scraping and phrase mining was done by cshang4.

Implementing BM25 and interpreting the results was done by jianing2 and siqig2.




