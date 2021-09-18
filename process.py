from fuzzywuzzy import fuzz
from fuzzywuzzy import process



# Penghitungan Leveinsthein distance, menggunakan library fuzzywuzy
def match_term(term, list_names, min_score=0):
    max_score =-1
    max_name=""

    for term2 in list_names:
        score = fuzz.ratio(term, term2)
        if (score > min_score) & (score > max_score):
            max_name = term2
            max_score = score
    return (max_name, max_score)