import nltk
from nltk.tokenize.treebank import TreebankWordDetokenizer
from nltk.corpus import stopwords
import string
import re


class Preprocessing(object):
    def __init__(self, raw):
        self.raw = raw

    @staticmethod
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
  
   
   

# print(preprocessing("cara bacaan idhar"))  


# hasil = Preprocessing.preprocessing("idiom")
# print(hasil)