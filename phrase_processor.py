import pickle

# phrases are found by running https://github.com/shangjingbo1226/AutoPhrase
# on all of the cached reviews. This is done manually and phrases are saved
# into a pickle file.



def phrase_replace(input_string):
  phrases = set()
  output = input_string
  try:
    phrases = pickle.load(file('other_data/phrases.p', 'rb'))
  except:
    phrases = set()
  
  for phrase in phrases:
    if phrase in output:
      output.replace(phrase, phrase.replace(' ', '_'))
  return output
      
