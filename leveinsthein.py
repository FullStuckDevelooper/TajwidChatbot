from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from preProcessing import Preprocessing


class Leveinsthein(object):
    def __init__(self, term,list_names, min_score=0):
        self.term = term
        self.list_names = list_names
        self.min_score = min_score


    @staticmethod
    def match_term(term, list_names, min_score=0):
        max_score =-1
        max_name=""

        for term2 in list_names:
            score = fuzz.ratio(Preprocessing.preprocessing(term), term2)
            if (score > min_score) & (score > max_score):
                max_name = term2
                max_score = score
        return (max_name, max_score)



