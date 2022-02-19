import telebot
import os
import random
from dict import tajwid_dict
from process import match_term

API_KEY = os.getenv('API_KEY')
bot =telebot.TeleBot('1673764376:AAH7kfxOVg5mgn_5ApqO7zcrYbiWWHy61c4')




@bot.message_handler(commands=['about'])
def greet(message):
    about = f"Ini adalah sebuah aplikasi yang bertujuan untuk memberikan informasi tajwid dasar kepada penggunanya, cukup ketikan pertanyaan yang ingin anda tanyakan.\nDibuat untuk menyelesaikan  tugas studi S1 teknik Informatika"
    bot.send_message(message.chat.id, about)
    
@bot.message_handler(commands=['random'])
def greet(message):
    bot.send_message(message.chat.id, random.choice(list(tajwid_dict.values())))

@bot.message_handler(commands=['help'])
def greet(message):
    bantuan = f'''-----------------------LIST COMMAND YANG TERSEDIA-----------------------
    \n/about : Berfungsi memberikan Informasi tentang aplikasi chatbot tajwid ini
    \n/help : Berfungsi untuk memberikan informasi tentang command yang tersedia pada aplikasi ini
    \n/random : Berfungsi untuk memberikan informasi acak yang berhubungan dengan tajwid 
    \nUntuk melakukan pertanyaan, cukup ketikan pertanyaan anda tanpa menggunakan Command apapun'''
    bot.send_message(message.chat.id, bantuan)


@bot.message_handler(content_types=['text'])
def tajwid(message):
    
    levDist =match_term(message.text, tajwid_dict.keys(), min_score= 50)

    if levDist[0]=="":
        bot.reply_to(message, "Maaf Jawaban tidak ditemukan")
    else:
        jawab = tajwid_dict[levDist[0]]
        # score = levDist[1]
        score = f"Similarity : {levDist[1]} %"
        bot.reply_to(message, jawab)
        bot.send_message(message.chat.id, score )
        print(levDist[1])  #debuging proses



print("Running")
bot.polling()









# print(fuzz.ratio("Apa Pengertian Idzhar", "Pengertian dari Idzhar"))
# print(fuzz.ratio("Apa Pegetian Idghom", "Pengertian dari Idzhar"))
# print("idhar memiliki 6 huruf yaitu hamzah(ء), ha'(ه), haa'(ح), kho'(خ), 'ain(ع), ghoin(غ) ) ")



# test =["apa pengertian tajwid","apa pengertian idhar","berapa huruf idhar","bagaimana cara membaca idhar","contoh bacaan idhar","apa pengertian idghom","bagaimana cara membaca idghom","contoh bacaan idghom"]

# print(match_term("apa pengertian tjwdi", test, min_score= 50))