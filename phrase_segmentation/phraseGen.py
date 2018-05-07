import os


# This is normally stored in the Autophrase directory 
# Combines all of the saves review texts into a single file 
# for consumption by autophrase.
path = '../ReviewComparer/reviews/'
with open('data/all_reviews.txt', 'w') as f:
  for i in os.listdir(path):
    with open(path + i, 'r') as reviewf:
      f.write(reviewf.read())
      

