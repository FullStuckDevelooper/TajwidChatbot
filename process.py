from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import nltk
from nltk.tokenize.treebank import TreebankWordDetokenizer
from nltk.corpus import stopwords
import string
import re

#Preprocessing
def preprocessing(raw):
    # Lower case
   hasil= raw.lower()
  
    # tokenize dan penghapusan tanda baca
   hasil = re.sub(r"\d+", "",hasil)
   trantab = str.maketrans(dict.fromkeys(list(string.punctuation)))  #penghapusan tanda baca
  
   hasil= hasil.translate(trantab)
   hasil= nltk.word_tokenize(hasil)
   #stopword
   list_stopwords = set(stopwords.words('indonesian'))
   list_stopwords.remove('cara')
   clean_data = [word for word in hasil if not word in list_stopwords]


   return TreebankWordDetokenizer().detokenize(clean_data)




# Penghitungan Leveinsthein distance, menggunakan library fuzzywuzy
def match_term(term, list_names, min_score=0):
    max_score =-1
    max_name=""

    for term2 in list_names:
        score = fuzz.ratio(preprocessing(term), term2)
        if (score > min_score) & (score > max_score):
            max_name = term2
            max_score = score
    return (max_name, max_score)


# a= "asu sua suu suu ?1...???"
# trantab = str.maketrans(dict.fromkeys(list(string.punctuation)))
# a= a.translate(trantab)
# a = re.sub(r"\d+", "",a)
# print(nltk.word_tokenize(a))

# print(preprocessing("cara bacaan idhar"))
