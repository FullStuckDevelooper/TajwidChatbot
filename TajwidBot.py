from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import telebot
import os

API_KEY = os.getenv('API_KEY')
bot =telebot.TeleBot('1673764376:AAH7kfxOVg5mgn_5ApqO7zcrYbiWWHy61c4')


# @bot.message_handler(commands=['Greet'])
# def greet(message):
#     bot.reply_to(message, "Idghom Bigunnah, Nun Mati bertemu Ya, فَمَنْ يَّعْمَلْ dibaca  FAMAYYA'MAL tidak boleh dibaca  FAMAN YA'MAL \n Idghom Bilagunnah,Tanwin bertemu Lam, رِ زْ قًا لَّكُمْ dibaca RIZQOLLAKUM")

# print("Running")
# bot.polling()


print(fuzz.ratio("Apa Pengertian Idzhar", "Pengertian dari Idzhar"))
print(fuzz.ratio("Apa Pegetian Idghom", "Pengertian dari Idzhar"))
print("idhar memiliki 6 huruf yaitu hamzah(ء), ha'(ه), haa'(ح), kho'(خ), 'ain(ع), ghoin(غ) ) ")


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

print(match_term("apa pengertian tjwdi", test, min_score= 50))