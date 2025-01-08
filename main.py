import os
import datetime
from telebot import telebot, types
import shutil
from yt_dlp import YoutubeDL
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from downloader import downloadMP3
from downloader import downloadWAV
from downloader import YTdownloadVideo480p
from downloader import YTdownloadVideo720p
from downloader import YTdownloadVideo1080p
from downloader import downloadVideoClip
from downloader import downloadVideoYTClip
from DbContexts import DbContext_saveuser
from DbContexts import DbContext_setlanguage
from DbContexts import DbContext_language

BOT_TOKEN = '8141165303:AAHfvsuUVZz6pDfOvGFR0Q2X6pgp6SsmV-w'
bot = telebot.TeleBot(BOT_TOKEN)

commands_eng = [
    types.BotCommand("start", "Start"),
    types.BotCommand("language", "Select language"),
]

commands_rus = [
    types.BotCommand("start", "Запустить"),
    types.BotCommand("language", "Выбрать язык"),
]
bot.set_my_commands(commands_eng)


@bot.message_handler(commands=['start'])
def startCommand(message):
    DbContext_saveuser(message.chat.id)
    language = DbContext_language(message.chat.id)
    print(f'{message.chat.id}    {language}')
    if language == 'english':
        bot.send_message(message.chat.id, "Send a link to your video")
        bot.set_my_commands(commands_eng)
    elif language == 'russian':
        bot.send_message(message.chat.id, "Отправьте ссылку на видео")
        bot.set_my_commands(commands_rus)
    else:
        langCommand(message)

#LANGUAGE
@bot.message_handler(commands=['language'])
def langCommand(message):
    DbContext_saveuser(message.chat.id)
    language = DbContext_language(message.chat.id)
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('English 🇬🇧', callback_data='eng'))
    markup.add(InlineKeyboardButton('Русский 🇷🇺', callback_data='rus'))
    if (language == 'russian'):
        bot.send_message(message.chat.id, "Выберите язык", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Select your language", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data in ['eng', 'rus'])
def handle_language(call):
    bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'eng':
        language = 'english'
        DbContext_setlanguage(language, call.message.chat.id)
        bot.send_message(call.message.chat.id, 'You’ve selected English')
        bot.set_my_commands(commands_eng)
    if call.data == 'rus':
        language = 'russian'
        bot.send_message(call.message.chat.id, 'Вы выбрали Русский')
        DbContext_setlanguage(language, call.message.chat.id)
        bot.set_my_commands(commands_rus)
    

#LINK HANDLER
sent_links = {}
@bot.message_handler(func=lambda msg: True) 
def link_handler(message):
    language = DbContext_language(message.chat.id)
    markup_YTclip_rus = InlineKeyboardMarkup()
    markup_YTclip_eng = InlineKeyboardMarkup()
    markup_clip_eng = InlineKeyboardMarkup()
    markup_clip_rus = InlineKeyboardMarkup()
    markup_eng = InlineKeyboardMarkup()
    markup_rus = InlineKeyboardMarkup()
    markup_YTclip_eng.add(InlineKeyboardButton('Audio', callback_data='mp3_clip'))
    markup_YTclip_eng.add(InlineKeyboardButton('Video', callback_data='mp4_YTclip'))
    markup_YTclip_rus.add(InlineKeyboardButton('Аудио', callback_data='mp3_clip'))
    markup_YTclip_rus.add(InlineKeyboardButton('Видео', callback_data='mp4_YTclip'))
    markup_clip_eng.add(InlineKeyboardButton('Audio', callback_data='mp3_clip'))
    markup_clip_eng.add(InlineKeyboardButton('Video', callback_data='mp4_clip'))
    markup_clip_rus.add(InlineKeyboardButton('Аудио', callback_data='mp3_clip'))
    markup_clip_rus.add(InlineKeyboardButton('Видео', callback_data='mp4_clip'))
    markup_eng.add(InlineKeyboardButton('Audio MP3', callback_data='mp3'))
    markup_eng.add(InlineKeyboardButton('Audio WAV', callback_data='wav'))
    markup_eng.add(InlineKeyboardButton('Video 480p', callback_data='mp4_480'))
    markup_eng.add(InlineKeyboardButton('Video 720p', callback_data='mp4_720'))
    markup_eng.add(InlineKeyboardButton('Video 1080p', callback_data='mp4_1080'))
    markup_rus.add(InlineKeyboardButton('Аудио MP3', callback_data='mp3'))
    markup_rus.add(InlineKeyboardButton('Аудио WAV', callback_data='wav'))
    markup_rus.add(InlineKeyboardButton('Видео 480p', callback_data='mp4_480'))
    markup_rus.add(InlineKeyboardButton('Видео 720p', callback_data='mp4_720'))
    markup_rus.add(InlineKeyboardButton('Видео 1080p', callback_data='mp4_1080'))
    if any(keyword in message.text for keyword in ['tiktok.com', 'instagram.com', 'youtube.com', 'youtu.be', 'youtube.com/shorts']):
        if any(keyword in message.text for keyword in ['tiktok.com', 'instagram.com']):
            if(language == 'russian'):
                bot.send_message(message.chat.id, "Выберите формат", reply_markup=markup_clip_rus)
            else:
                bot.send_message(message.chat.id, "Choose a format", reply_markup=markup_clip_eng)
            sent_links[message.chat.id] = message.text
        elif any(keyword in message.text for keyword in ['youtube.com/shorts']):
            if(language == 'russian'):
                bot.send_message(message.chat.id, "Выберите формат", reply_markup=markup_YTclip_rus)
            else:
                bot.send_message(message.chat.id, "Choose a format", reply_markup=markup_YTclip_eng)
            sent_links[message.chat.id] = message.text
        else:
            if(language == 'russian'):
                bot.send_message(message.chat.id, "Выберите формат", reply_markup=markup_rus)
            else:
                bot.send_message(message.chat.id, "Choose a format", reply_markup=markup_eng)
            sent_links[message.chat.id] = message.text
    else:
        if(language == 'russian'):
            bot.reply_to(message, "Недействительная ссылка")
        else:
            bot.reply_to(message, "Invalid link")


@bot.callback_query_handler(func=lambda call: call.data in ['mp3', 'wav', 'mp4_720', 'mp4_1080', 'mp4_480', 'mp4_clip', 'mp3_clip', 'mp4_YTclip'])
def format_callback(call):
    language = DbContext_language(call.message.chat.id)
    bot.delete_message(call.message.chat.id, call.message.message_id)
    current_url = sent_links[call.message.chat.id].split('&')[0]
    current_id = call.message.chat.id
    if call.data == 'mp3':
        if(language == 'russian'):
            downloading_message = bot.send_message(call.message.chat.id, "Аудио MP3 загружается...")
        else:
            downloading_message = bot.send_message(call.message.chat.id, "The MP3 audio is downloading...")
        downloadMP3(current_url, current_id, bot, language)
        bot.delete_message(call.message.chat.id, downloading_message.message_id)

    elif call.data == 'wav':
        if(language == 'russian'):
            downloading_message = bot.send_message(call.message.chat.id, "Аудио WAV загружается...")
        else:
            downloading_message = bot.send_message(call.message.chat.id, "The WAV audio is downloading...")
        downloadWAV(current_url, current_id, bot, language)
        bot.delete_message(call.message.chat.id, downloading_message.message_id)
    
    elif call.data == 'mp4_480':
        if(language == 'russian'):
            downloading_message = bot.send_message(call.message.chat.id, "Видео 480p загружается...")
        else:
            downloading_message = bot.send_message(call.message.chat.id, "The 480p video is downloading...")
        YTdownloadVideo480p(current_url, current_id, bot, language)
        bot.delete_message(call.message.chat.id, downloading_message.message_id)

    elif call.data == 'mp4_720':
        if(language == 'russian'):
            downloading_message = bot.send_message(call.message.chat.id, "Видео 720p загружается...")
        else:
            downloading_message = bot.send_message(call.message.chat.id, "The 720p video is downloading...")
        YTdownloadVideo720p(current_url, current_id, bot, language)
        bot.delete_message(call.message.chat.id, downloading_message.message_id)

    elif call.data == 'mp4_1080':
        if(language == 'russian'):
            downloading_message = bot.send_message(call.message.chat.id, "Видео 1080p загружается...")
        else:
            downloading_message = bot.send_message(call.message.chat.id, "The 1080p video is downloading...")
        YTdownloadVideo1080p(current_url, current_id, bot, language)
        bot.delete_message(call.message.chat.id, downloading_message.message_id)

    elif call.data == 'mp4_clip':
        if(language == 'russian'):
            downloading_message = bot.send_message(call.message.chat.id, "Видео загружается...")
        else:
            downloading_message = bot.send_message(call.message.chat.id, "The video is downloading...")
        downloadVideoClip(current_url, current_id, bot, language)
        bot.delete_message(call.message.chat.id, downloading_message.message_id)
    
    elif call.data == 'mp4_YTclip':
        if(language == 'russian'):
            downloading_message = bot.send_message(call.message.chat.id, "Видео загружается...")
        else:
            downloading_message = bot.send_message(call.message.chat.id, "The video is downloading...")
        downloadVideoYTClip(current_url, current_id, bot, language)
        bot.delete_message(call.message.chat.id, downloading_message.message_id)

    elif call.data == 'mp3_clip':
        if(language == 'russian'):
            downloading_message = bot.send_message(call.message.chat.id, "Аудио загружается...")
        else:
            downloading_message = bot.send_message(call.message.chat.id, "The audio is downloading...")
        downloadMP3(current_url, current_id, bot, language)
        bot.delete_message(call.message.chat.id, downloading_message.message_id)

    print(f'{current_id} Request is Done      [{datetime.datetime.now()}]')



if __name__ == '__main__':
    print("Bot is running...")
    bot.infinity_polling()