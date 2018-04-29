import pickle

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
      
