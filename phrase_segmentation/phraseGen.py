import os

path = '../ReviewComparer/reviews/'
with open('data/all_reviews.txt', 'w') as f:
  for i in os.listdir(path):
    with open(path + i, 'r') as reviewf:
      f.write(reviewf.read())
      

