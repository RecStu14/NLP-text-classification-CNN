#HELPER FUNCTIONS TO AID IN IMPORTING INSTEAD OF REWRITING
import string
import re

#remove url if present
def remove_url(text):
  url_pattern  = re.compile('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
  return url_pattern.sub(r'', text)

#remove punctuations
def clean_text(text):
  delete_dict = {sp_character: '' for sp_character in string.punctuation} 
  delete_dict[' '] = ' ' 
  table = str.maketrans(delete_dict)
  text1 = text.translate(table)
  
  textArr= text1.split()
  text2 = ' '.join([w for w in textArr if ( not w.isdigit() and  ( not w.isdigit() and len(w)>2))]) 
  
  return text2.lower()