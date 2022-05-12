import telebot
import os
import random
from dict import tajwid_dict
from process import match_term
from leveinsthein import Leveinsthein

class System:
    def __init__(self):
        self.bot = telebot.TeleBot('1673764376:AAH7kfxOVg5mgn_5ApqO7zcrYbiWWHy61c4')
        self.init_handler()
    

    def init_handler(self):

        @self.bot.message_handler(commands=['start'])
        def greet(message):
            about = f"Selamat Datang di TajwidChatbot, silahkan tuliskan pertanyaan anda :)"
            self.bot.send_message(message.chat.id, about)
        

        @self.bot.message_handler(commands=['about'])
        def greet(message):
            about = f"Ini adalah sebuah aplikasi yang bertujuan untuk memberikan informasi tajwid dasar kepada penggunanya, cukup ketikan pertanyaan yang ingin anda tanyakan.\nDibuat untuk menyelesaikan  tugas studi S1 teknik Informatika"
            self.bot.send_message(message.chat.id, about)

        @self.bot.message_handler(commands=['random'])
        def greet(message):
            self.bot.send_message(message.chat.id, random.choice(list(tajwid_dict.values())))

        @self.bot.message_handler(commands=['help'])
        def greet(message):
            bantuan = f'''-----------------------LIST COMMAND YANG TERSEDIA-----------------------
            \n/about : Berfungsi memberikan Informasi tentang aplikasi chatbot tajwid ini
            \n/help : Berfungsi untuk memberikan informasi tentang command yang tersedia pada aplikasi ini
            \n/random : Berfungsi untuk memberikan informasi acak yang berhubungan dengan tajwid 
            \nUntuk melakukan pertanyaan, cukup ketikan pertanyaan anda tanpa menggunakan Command apapun'''
            self.bot.send_message(message.chat.id, bantuan)

        @self.bot.message_handler(content_types=['text'])
        def tajwid(message):
            
            levDist =Leveinsthein.match_term(message.text, tajwid_dict.keys(), min_score= 50)

            if levDist[0]=="":
                self.bot.reply_to(message, "Maaf Jawaban tidak ditemukan")
            else:
                jawab = tajwid_dict[levDist[0]]
                # score = levDist[1]
                score = f"Similarity : {levDist[1]} %"
                self.bot.reply_to(message, jawab)
                self.bot.send_message(message.chat.id, score )
                print(levDist[1])  #debuging proses
        
    def start_bot(self):
        print("Running")
        self.bot.polling()
        
        
        
        