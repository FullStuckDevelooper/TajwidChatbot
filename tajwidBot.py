import telebot
import os
import random
from dict import tajwid_dict
from process import match_term

API_KEY = os.getenv('API_KEY')
bot =telebot.TeleBot('1673764376:AAH7kfxOVg5mgn_5ApqO7zcrYbiWWHy61c4')




@bot.message_handler(commands=['Greet'])
def greet(message):
    bot.reply_to(message, "Contoh bacaan mad wajib muttashil, ketika mad tobii bertemu huruf hamzah اِذَا جَآءَ dibaca izajaa-a (5 harkat)")
    
@bot.message_handler(commands=['random'])
def greet(message):
    bot.reply_to(message, random.choice(list(tajwid_dict.values())))


@bot.message_handler(content_types=['text'])
def tajwid(message):
    
    levDist =match_term(message.text, tajwid_dict.keys(), min_score= 50)

    if levDist[0]=="":
        bot.reply_to(message, "Maaf Jawaban tidak ditemukan")
    else:
        jawab = tajwid_dict[levDist[0]]
        score = levDist[1]
        bot.reply_to(message, jawab)
        bot.reply_to(message, score)
        print(levDist[1])  #debuging proses



print("Running")
bot.polling()









# print(fuzz.ratio("Apa Pengertian Idzhar", "Pengertian dari Idzhar"))
# print(fuzz.ratio("Apa Pegetian Idghom", "Pengertian dari Idzhar"))
# print("idhar memiliki 6 huruf yaitu hamzah(ء), ha'(ه), haa'(ح), kho'(خ), 'ain(ع), ghoin(غ) ) ")



# test =["apa pengertian tajwid","apa pengertian idhar","berapa huruf idhar","bagaimana cara membaca idhar","contoh bacaan idhar","apa pengertian idghom","bagaimana cara membaca idghom","contoh bacaan idghom"]

# print(match_term("apa pengertian tjwdi", test, min_score= 50))