from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import telebot
import os


tajwid_dict = {


"apa pengertian tajwid": "ilmu tajwid adalah ilmu yang digunakan untuk mengetahui kaiddah dan cara membaca huruf-huruf Al-Quran secara baik dan benar",

"apa pengertian idhar":"idhar merupakan bagian tajwid dari nun mati atau tanwin, idhar artinya menjelaskan",
"berapa huruf idhar":"idhar memiliki 6 huruf yaitu hamzah(ء), ha'(ه), haa'(ح), kho'(خ), 'ain(ع), ghoin(غ) ) ",
"bagaimana cara membaca idhar":"cara membaca idhar harus terang jelas dan pendek, bunyi suaranya tetap jelas, tidak samar serta tidak mendengung.",
"contoh bacaan idhar": "Nun mati bertemu huruf Ha, مِنْهُمْ  dibaca MIN HUM",

"apa pengertian idghom":"idhghom merupakan bagian tajwid dari nun mati atau tanwin, idghom artinya memasukan atau mentasydidkan, idghom dibagi menjadi 2 bagian yaitu Bigunah(dengan mendengung) dan bilagunah (tanpa Mendengung)",
"berapa huruf idghom":"idghom memiliki 6 huruf yaitu 4 Huruf untuk Bigunnah yaitu Ya(ي), Nun(ن), Mim(م), Wau(و) serta 2 Huruf Untuk Bilagunah yaitu Lam(ل), Ra(ر)",
"bagaimana cara membaca idghom":"cara membaca idghom harus dimasukan menjadi satu huruf dengan huruf sesudahnya atau ditasydidkannya",
"contoh bacaan idghom":"Idghom Bigunnah, Nun Mati bertemu Ya, فَمَنْ يَّعْمَلْ dibaca  FAMAYYA'MAL tidak boleh dibaca  FAMAN YA'MAL \n Idghom Bilagunnah,Tanwin bertemu Lam, رِ زْ قًا لَّكُمْ dibaca RIZQOLLAKUM",
"":"",
"":"",
"":"",

}

# test =["apa pengertian tajwid","apa pengertian idhar","berapa huruf idhar","bagaimana cara membaca idhar","contoh bacaan idhar","apa pengertian idghom","bagaimana cara membaca idghom","contoh bacaan idghom"]
# print(process.extract("pengertian idgom", tajwid_dict.keys(), limit=1))
# print(fuzz.ratio("pengertian idgom", "apa pengertian idghom"))

def match_term(term, list_names, min_score=0):
    max_score =-1
    max_name=""

    for term2 in list_names:
        score = fuzz.ratio(term, term2)
        if (score > min_score) & (score > max_score):
            max_name = term2
            max_score = score
    return (max_name, max_score)

test =["apa pengertian tajwid","apa pengertian idhar","berapa huruf idhar","bagaimana cara membaca idhar","contoh bacaan idhar","apa pengertian idghom","bagaimana cara membaca idghom","contoh bacaan idghom"]

x =match_term("apa pengertian tjwdi", tajwid_dict.keys(), min_score= 50)
jawab = tajwid_dict[x[0]]
print(jawab)

