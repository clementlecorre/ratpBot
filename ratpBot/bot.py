#!/usr/bin/env python
# encoding: utf-8
# Store : https://storebot.me/bot/ratpbot

import telebot
import os
from telebot import types
import re
import search
import requests
import time

# Emojis icon
metro = u'\U0001F689'
star = u'\U00002B50'
smile = u'\U0001F609'
CRYINGFACE = u'\U0001F622'

# API_TOKEN -> @botfather
# https://telegram.me/botfather
# Example API : 110201543:AAHdqTcvCH1vGWJxfSeofSAs0K5PALDsaw
API_TOKEN = os.environ['API_TOKEN']

bot = telebot.TeleBot(API_TOKEN)

ratp_dict = {}

class Ratp:
    def __init__(self, transport):
        self.transport = transport
        self.line = None
        self.stations = None
        self.destination = None

bot = telebot.TeleBot(API_TOKEN)

# Handle '/start'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """ Hi ! A bot that will provide schedules and alerts for RATP trains, subways, and buses in France. """)

# /help
@bot.message_handler(commands=['help'])
def help(message):
   cid = message.chat.id
   bot.reply_to(message, """Type /metro ligne arret destination\n  Type /tram ligne arret destination\n  Type /rer ligne arret  destination\n  Type /bus ligne arret  destination\n  Type /noctilien ligne arret  destination """)

# Handle '/metro' or '/m' or '/Metro'
@bot.message_handler(commands=['metro','m', 'Metro'])
def metro(message):
    cid = message.chat.id
    bot.send_chat_action(cid, 'typing')
    destination = None
    stations = None
    options = message.text
    if options:
        options = re.findall(r'\S+', options)
        if len(options) == 3:
            bot.send_message(cid, search.extractInformation("metro", str(options[1]), str(options[2]), destination) )
        if len(options) == 4:
            bot.send_message(cid, search.extractInformation("metro", str(options[1]), str(options[2]), str(options[3])) )
        if len(options) == 2:
            bot.send_message(cid, search.extractInformation("metro", str(options[1]), stations, destination) )
        if len(options) == 1:
            bot.send_message(cid, " Attention tu t'es trompé dans la syntax ! ^^ \n Exemple : \n /Metro 13 invalide Courtille")


# Handle '/tram' or 't' or '/Tram'
@bot.message_handler(commands=['Tram','tram', 't'])
def tram(message):
    cid = message.chat.id
    bot.send_chat_action(cid, 'typing')
    destination = None
    stations = None
    options = message.text
    if options:
        options = re.findall(r'\S+', options)
        if len(options) == 3:
            bot.send_message(cid, search.extractInformation("tram", str(options[1]), str(options[2]), destination) )
        if len(options) == 4:
            bot.send_message(cid, search.extractInformation("tram", str(options[1]), str(options[2]), str(options[3])) )
        if len(options) == 2:
            bot.send_message(cid, search.extractInformation("tram", str(options[1]), stations, destination) )
        if len(options) == 1:
            bot.send_message(cid, "Attention tu t'es trompé dans la syntax ! ^^ \n Exemple : \n /tram T1 village Noisy")

# Handle '/rer' or '/Rer'
@bot.message_handler(commands=['Rer','rer'])
def rer(message):
    cid = message.chat.id
    bot.send_chat_action(cid, 'typing')
    destination = None
    stations = None
    options = message.text
    if options:
        options = re.findall(r'\S+', options)
        if len(options) == 3:
            bot.send_message(cid, search.extractInformation("rer", str(options[1]), str(options[2]), destination) )
        if len(options) == 4:
            bot.send_message(cid, search.extractInformation("rer", str(options[1]), str(options[2]), str(options[3])) )
        if len(options) == 2:
            bot.send_message(cid, search.extractInformation("rer", str(options[1]), stations, destination) )
        if len(options) == 1:
            bot.send_message(cid, "Attention tu t'es trompé dans la syntax ! ^^ \n Exemple : \n /rer a nation")

# Handle '/bus' or '/Bus' or '/b'
@bot.message_handler(commands=['Bus','bus', 'b'])
def bus(message):
    cid = message.chat.id
    bot.send_chat_action(cid, 'typing')
    destination = None
    stations = None
    options = message.text
    if options:
        options = re.findall(r'\S+', options)
        if len(options) == 3:
            bot.send_message(cid, search.extractInformation("bus", str(options[1]), str(options[2]), destination) )
        if len(options) == 4:
            bot.send_message(cid, search.extractInformation("bus", str(options[1]), str(options[2]), str(options[3])) )
        if len(options) == 2:
            bot.send_message(cid, search.extractInformation("bus", str(options[1]), stations, destination) )
        if len(options) == 1:
            bot.send_message(cid, "Attention tu t'es trompé dans la syntax ! ^^ \n Exemple : \n /bus 137 Mairie")


# Handle '/noctilien' or '/Noctilien'
@bot.message_handler(commands=['noctilien','Noctilien', 'n'])
def noctilien(message):
    cid = message.chat.id
    bot.send_chat_action(cid, 'typing')
    destination = None
    stations = None
    options = message.text
    if options:
        options = re.findall(r'\S+', options)
        if len(options) == 3:
            bot.send_message(cid, search.extractInformation("noctilien", str(options[1]), str(options[2]), destination) )
        if len(options) == 4:
            bot.send_message(cid, search.extractInformation("noctilien", str(options[1]), str(options[2]), str(options[3])) )
        if len(options) == 2:
            bot.send_message(cid, search.extractInformation("noctilien", str(options[1]), stations, destination) )
        if len(options) == 1:
            bot.send_message(cid, "Attention tu t'es trompé dans la syntax ! ^^ \n Exemple : \n /noctilien ligne arret")

# Handle '/alert'
@bot.message_handler(commands=['alert'])
def alert(message):
    cid = message.chat.id
    bot.send_chat_action(cid, 'typing')
    options = message.text
    if options:
        options = re.findall(r'\S+', options)
        if len(options) == 3:
            bot.send_message(cid, search.getDisturbance(str(options[1]), str(options[2]) ))
        if len(options) == 1:
            bot.send_message(cid, "Attention tu t'es trompé dans la syntax ! ^^ \n Exemple : \n /alert {manif, travaux, alerte} {metro,tram,rer} \n /alert manif metro")

# /about
@bot.message_handler(commands=['about'])
def about(message):
   cid = message.chat.id
   bot.reply_to(message, "Bot developed in python3 by @cl3m3nt \n Share bot https://storebot.me/bot/ratpbot \n Source code : https://github.com/cl3m3nt666/ratpBot \n\n If you like our bot, please put " + star + star + star + star + star +  " in the storebot " + smile )



# Handle '/go'
@bot.message_handler(commands=['go'])
def send_go(message):
    cid = message.chat.id
    transport = "metro"
    user = Ratp(transport)
    ratp_dict[cid] = user
    msg = bot.reply_to(message, "Heee salut tu veux prendre le metro, rer, tram, bus ou noctilien ?  " + smile + smile )
    bot.register_next_step_handler(msg, processTransportStep)

def processTransportStep(message):
    try:
        cid = message.chat.id
        user = ratp_dict[cid]
        user.transport = message.text
        #if message.text not in ("metro", "tram", "rer", "noctilien", "bus"):
        if message.text == "noctilien":
            msg = bot.reply_to(message, 'Quelle ligne de ' + user.transport +  ' ? Ahh tu rentre encore de soirée ! ')
        else:
            msg = bot.reply_to(message, 'Quelle ligne de ' + user.transport + ' ?')
        bot.register_next_step_handler(msg, processLineStep)
    except Exception as e:
        bot.reply_to(message, CRYINGFACE + ' oooops je suis trop fatigué pour y arriver..')

def processLineStep(message):
    try:
        cid = message.chat.id
        user = ratp_dict[cid]
        user.line = message.text
        msg = bot.reply_to(message, 'Quel arret pour la ligne de ' + user.transport + ' '+  user.line +  ' ?')
        bot.register_next_step_handler(msg, processStationsStep)
    except Exception as e:
        bot.reply_to(message, CRYINGFACE + ' oooops je suis trop fatigué pour y arriver..')

def processStationsStep(message):
    try:
        cid = message.chat.id
        bot.send_chat_action(cid, 'typing')
        user = ratp_dict[cid]
        user.stations = message.text
        destination = None
        bot.send_message(cid, search.extractInformation(user.transport, user.line ,user.stations , user.destination))
    except Exception as e:
        bot.reply_to(message, CRYINGFACE + ' oooops je suis trop fatigué pour y arriver.. Ressaye! ' + str(e))


while True:
    try:
        print ("bot.polling()")
        bot.polling(none_stop=True, interval=3)
    except (requests.exceptions.ConnectionError, requests.exceptions.ReadTimeout) as e: # HTTPSConnectionPool(host='api.telegram.org', port=443): Max retries exceeded with url:
        print (str(e) + "\n")
        time.sleep(15) # used to avoid temporary errors
        exit (1) # run.sh, re-run bot.py
    except Exception as e:
        print (traceback.format_exc())
        exit(1)
