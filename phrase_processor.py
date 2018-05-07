import pickle

# multi-word phrases are found by running https://github.com/shangjingbo1226/AutoPhrase
# on all of the cached reviews. This is done manually and phrases are saved
# into a pickle file.


# takes an input string and finds all multi-word phrases
# replaces the spaces in those strings with underscores
def phrase_replace(input_string):
  phrases = set()
  output = input_string
  phrases = pickle.load(open('phrase_segmentation/phrases.p', 'rb'))
  for phrase in phrases:
    if phrase in output:
      output = output.replace(phrase, phrase.replace(' ', '_'))
  return output
      
