from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import nltk
from nltk.tokenize.treebank import TreebankWordDetokenizer
import string

#Preprocessing
def preprocessing(raw):
    # Lower case
   hasil= raw.lower()
  
    # tokenize dan penghapusan tanda baca
   trantab = str.maketrans(dict.fromkeys(list(string.punctuation)))
   hasil= hasil.translate(trantab)
   hasil= nltk.word_tokenize(hasil)
    #stopword



   return TreebankWordDetokenizer().detokenize(hasil)




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


# a= "asu sua suu suu ????"
# trantab = str.maketrans(dict.fromkeys(list(string.punctuation)))
# a= a.translate(trantab)

# print(nltk.word_tokenize(a))

# print(preprocessing("MANDI SAMA KAMU BAU IHH !!!! ..00009090889"))
