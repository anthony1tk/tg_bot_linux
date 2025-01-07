import os
import telebot
import shutil
from yt_dlp import YoutubeDL
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def downloadMP3(url, id, bot, language):
    print(url)
    print(id)
    chat_folder = str(id)
    os.makedirs(chat_folder, exist_ok=True)
    try:
        options_title = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',    
            }],
            'outtmpl': os.path.join(chat_folder, '%(title)s.%(ext)s'),
            'cookies': 'cookie.json'
        }
        options_id = {
            'format': 'bestaudio/best',

            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3'
            }],
         
            'outtmpl': os.path.join(chat_folder, '%(id)s.%(ext)s'),
            'cookies': 'cookie.json'
        }

        invalid_chars = set(r'\/:*?"<>|')

        with YoutubeDL() as ydl:
            info = ydl.extract_info(url, download=False)
        string_check = any(char in invalid_chars for char in info['title'])

        if (string_check == True):
            with YoutubeDL(options_id) as ydl:
                info = ydl.extract_info(url, download=True)
                mp3_file = f"{chat_folder}/{info['id']}.mp3"
                mp3_file_credits_path = f"{chat_folder}/{info['id']} @QuickMediaYoutubeBot.mp3" 
        else:
            with YoutubeDL(options_title) as ydl:
                info = ydl.extract_info(url, download=True)
                mp3_file = f"{chat_folder}/{info['title']}.mp3"
                mp3_file_credits_path = f"{chat_folder}/{info['title']} @QuickMediaYoutubeBot.mp3"

        os.rename(mp3_file, mp3_file_credits_path) 
        
        with open(mp3_file_credits_path, 'rb') as file:
            bot.send_audio(id, file)

    except Exception as e:
        if(language == 'russian'):
            bot.send_message(id, f"Ошибка. Попробуйте выбрать другой формат.")
        else:
            bot.send_message(id, f"An error occured. Try choosing a different format.")
    shutil.rmtree(chat_folder)

def downloadWAV(url, id, bot, language):
    print(url)
    print(id)
    chat_folder = str(id)
    os.makedirs(chat_folder, exist_ok=True)
    try:
        options_title = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'wav'
            }],
            'outtmpl': os.path.join(chat_folder, '%(title)s.%(ext)s'),
            'cookies': 'cookie.json'
        }
        options_id = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'wav'
            }],
            'outtmpl': os.path.join(chat_folder, '%(id)s.%(ext)s'),
            'cookies': 'cookie.json'
        }

        invalid_chars = set(r'\/:*?"<>|')

        with YoutubeDL() as ydl:
            info = ydl.extract_info(url, download=False)
        string_check = any(char in invalid_chars for char in info['title'])

        if (string_check == True):
            with YoutubeDL(options_id) as ydl:
                info = ydl.extract_info(url, download=True)
                mp3_file = f"{chat_folder}/{info['id']}.wav"
                mp3_file_credits_path = f"{chat_folder}/{info['id']} @QuickMediaYoutubeBot.mp3" 
        else:
            with YoutubeDL(options_title) as ydl:
                info = ydl.extract_info(url, download=True)
                mp3_file = f"{chat_folder}/{info['title']}.wav"
                mp3_file_credits_path = f"{chat_folder}/{info['id']} @QuickMediaYoutubeBot.mp3" 

        os.rename(mp3_file, mp3_file_credits_path)    

        with open(mp3_file_credits_path, 'rb') as file:
            bot.send_audio(id, file)

    except Exception as e:
        if(language == 'russian'):
            bot.send_message(id, f"Ошибка. Попробуйте выбрать другой формат.")
        else:
            bot.send_message(id, f"An error occured. Try choosing a different format.")
    shutil.rmtree(chat_folder)

def YTdownloadVideo1080p(url, id, bot, language):
    print(url)
    print(id)
    chat_folder = str(id)
    os.makedirs(chat_folder, exist_ok=True)
    try:
        options_title = {
            'format': 'bestvideo[width<=1080][vcodec=h264]+bestaudio[acodec=aac]/best',
            'max_filesize': 50 * 1024 * 1024,
            'merge_output_format': 'mp4',
            'postprocessors': [
                {
                    'key': 'FFmpegMetadata',  
                },
                {
                    'key': 'EmbedThumbnail',  
                    'already_have_thumbnail': False,
                },
            ],
            'outtmpl': os.path.join(chat_folder, '%(title)s.%(ext)s'),
            'cookies': 'cookie.json'
        }
        options_id = {
            'format': 'bestvideo[width<=1080][vcodec=h264]+bestaudio[acodec=aac]/best',
            'max_filesize': 50 * 1024 * 1024,
            'merge_output_format': 'mp4',
            'postprocessors': [
                {
                    'key': 'FFmpegMetadata',  
                },
                {
                    'key': 'EmbedThumbnail',  
                    'already_have_thumbnail': False,
                },
            ],
            'outtmpl': os.path.join(chat_folder, '%(id)s.%(ext)s'),
            'cookies': 'cookie.json'
        }

        invalid_chars = set(r'\/:*?"<>|')

        with YoutubeDL() as ydl:
            info = ydl.extract_info(url, download=False)
        string_check = any(char in invalid_chars for char in info['title'])

        if (string_check == True):
            with YoutubeDL(options_id) as ydl:
                info = ydl.extract_info(url, download=True)
        else:
            with YoutubeDL(options_title) as ydl:
                info = ydl.extract_info(url, download=True)
        file = ydl.prepare_filename(info) 

        with open(file, 'rb') as file:
            bot.send_video(chat_id=id, video=file, caption=f'{info['title']}\n@QuickMediaYoutubeBot', supports_streaming=True)

    except Exception as e:
        if(language == 'russian'):
            bot.send_message(id, f"Ошибка. Попробуйте выбрать другой формат.")
        else:
            bot.send_message(id, f"An error occured. Try choosing a different format.")
    shutil.rmtree(chat_folder)

def YTdownloadVideo720p(url, id, bot, language):
    print(url)
    print(id)
    chat_folder = str(id)
    os.makedirs(chat_folder, exist_ok=True)
    try:
        options_title = {
            'format': 'bestvideo[width<=720][vcodec=h264]+bestaudio[acodec=aac]/best',
            'max_filesize': 50 * 1024 * 1024,
            'merge_output_format': 'mp4',
            'postprocessors': [
                {
                    'key': 'FFmpegMetadata',  
                },
                {
                    'key': 'EmbedThumbnail',  
                    'already_have_thumbnail': False,
                },
            ],
            'outtmpl': os.path.join(chat_folder, '%(title)s.%(ext)s'),
            'cookies': 'cookie.json'
        }
        options_id = {
            'format': 'bestvideo[width<=720][vcodec=h264]+bestaudio[acodec=aac]/best',
            'max_filesize': 50 * 1024 * 1024,
            'merge_output_format': 'mp4',
            'postprocessors': [
                {
                    'key': 'FFmpegMetadata',  
                },
                {
                    'key': 'EmbedThumbnail',  
                    'already_have_thumbnail': False,
                },
            ],
            'write-thumbnail': True,
            'outtmpl': os.path.join(chat_folder, '%(id)s.%(ext)s'),
            'cookies': 'cookie.json'
        }

        invalid_chars = set(r'\/:*?"<>|')

        with YoutubeDL() as ydl:
            info = ydl.extract_info(url, download=False)
        string_check = any(char in invalid_chars for char in info['title'])

        if (string_check == True):
            with YoutubeDL(options_id) as ydl:
                info = ydl.extract_info(url, download=True)
        else:
            with YoutubeDL(options_title) as ydl:
                info = ydl.extract_info(url, download=True)
        file = ydl.prepare_filename(info)

        with open(file, 'rb') as file:
            bot.send_video(chat_id=id, video=file, caption=f'{info['title']}\n@QuickMediaYoutubeBot',supports_streaming=True)

    except Exception as e:
        if(language == 'russian'):
            bot.send_message(id, f"Ошибка. Попробуйте выбрать другой формат.")
        else:
            bot.send_message(id, f"An error occured. Try choosing a different format.")
    shutil.rmtree(chat_folder)

def YTdownloadVideo480p(url, id, bot, language):
    print(url)
    print(id)
    chat_folder = str(id)
    os.makedirs(chat_folder, exist_ok=True)
    try:
        options_title = {
            'format': 'bestvideo[width<=480][vcodec=h264]+bestaudio[acodec=aac]/best',
            'max_filesize': 50 * 1024 * 1024,
            'merge_output_format': 'mp4',
            'postprocessors': [
                {
                    'key': 'FFmpegMetadata',  
                },
                {
                    'key': 'EmbedThumbnail',  
                    'already_have_thumbnail': False,
                },
            ],
            'outtmpl': os.path.join(chat_folder, '%(title)s.%(ext)s'),
            'cookies': 'cookie.json'
        }
        options_id = {
            'format': 'bestvideo[width<=480][vcodec=h264]+bestaudio[acodec=aac]/best',
            'max_filesize': 50 * 1024 * 1024,
            'merge_output_format': 'mp4',
             'postprocessors': [
                {
                    'key': 'FFmpegMetadata',  
                },
                {
                    'key': 'EmbedThumbnail',  
                    'already_have_thumbnail': False,
                },
            ],
            'outtmpl': os.path.join(chat_folder, '%(id)s.%(ext)s'),
            'cookies': 'cookie.json'
        }

        invalid_chars = set(r'\/:*?"<>|')

        with YoutubeDL() as ydl:
            info = ydl.extract_info(url, download=False)
        string_check = any(char in invalid_chars for char in info['title'])

        if (string_check == True):
            with YoutubeDL(options_id) as ydl:
                info = ydl.extract_info(url, download=True)
        else:
            with YoutubeDL(options_title) as ydl:
                info = ydl.extract_info(url, download=True)
        file = ydl.prepare_filename(info)

        with open(file, 'rb') as file:
            bot.send_video(chat_id=id, video=file, caption=f'{info['title']}\n@QuickMediaYoutubeBot', supports_streaming=True)

    except Exception as e:
        if(language == 'russian'):
            bot.send_message(id, f"Ошибка. Попробуйте выбрать другой формат.")
        else:
            bot.send_message(id, f"An error occured. Try choosing a different format.")
    shutil.rmtree(chat_folder)

def downloadVideoClip(url, id, bot, language):
    print(url)
    print(id)
    chat_folder = str(id)
    os.makedirs(chat_folder, exist_ok=True)
    try:
        options_title = {
            'format': 'bestvideo+bestaudio[acodec=aac]/best',
            'max_filesize': 50 * 1024 * 1024,
            'write_thumbnail': True,
            'outtmpl': os.path.join(chat_folder, '%(title)s.%(ext)s'),
            'cookies': 'cookie.json'
        }
        options_id = {
            'format': 'bestvideo+bestaudio[acodec=aac]/best',
            'max_filesize': 50 * 1024 * 1024,
            'write_thumbnail': True,
            'outtmpl': os.path.join(chat_folder, '%(id)s.%(ext)s'),
            'cookies': 'cookie.json'
        }

        invalid_chars = set(r'\/:*?"<>|')

        with YoutubeDL() as ydl:
            info = ydl.extract_info(url, download=False)
        string_check = any(char in invalid_chars for char in info['title'])

        if (string_check == True):
            with YoutubeDL(options_id) as ydl:
                info = ydl.extract_info(url, download=True)
        else:
            with YoutubeDL(options_title) as ydl:
                info = ydl.extract_info(url, download=True)
        file = ydl.prepare_filename(info)

        with open(file, 'rb') as file:
            bot.send_video(chat_id=id, video=file, caption=f'{info['title']}\n@QuickMediaYoutubeBot', supports_streaming=True)

    except Exception as e:
        if(language == 'russian'):
            bot.send_message(id, f"Ошибка. Попробуйте выбрать другой формат.{str(e)}")
        else:
            bot.send_message(id, f"An error occured. Try choosing a different format.")
    shutil.rmtree(chat_folder)

def downloadVideoYTClip(url, id, bot, language):
    print(url)
    print(id)
    chat_folder = str(id)
    os.makedirs(chat_folder, exist_ok=True)
    try:
        options_title = {
            'format': 'bestvideo[vcodec=h264]+bestaudio[acodec=aac]/best',
            'max_filesize': 50 * 1024 * 1024,

            'write_thumbnail': True,
            'outtmpl': os.path.join(chat_folder, '%(title)s.%(ext)s'),
            'cookies': 'cookie.json'
        }
        options_id = {
            'format': 'bestvideo[vcodec=h264]+bestaudio[acodec=aac]/best',
            'max_filesize': 50 * 1024 * 1024,

            'write_thumbnail': True,
            'outtmpl': os.path.join(chat_folder, '%(id)s.%(ext)s'),
            'cookies': 'cookie.json'
        }

        invalid_chars = set(r'\/:*?"<>|')

        with YoutubeDL() as ydl:
            info = ydl.extract_info(url, download=False)
        string_check = any(char in invalid_chars for char in info['title'])

        if (string_check == True):
            with YoutubeDL(options_id) as ydl:
                info = ydl.extract_info(url, download=True)
        else:
            with YoutubeDL(options_title) as ydl:
                info = ydl.extract_info(url, download=True)
        file = ydl.prepare_filename(info)

        with open(file, 'rb') as file:
            bot.send_video(chat_id=id, video=file, caption=f'{info['title']}\n@QuickMediaYoutubeBot', supports_streaming=True)

    except Exception as e:
        if(language == 'russian'):
            bot.send_message(id, f"Ошибка. Попробуйте выбрать другой формат.")
        else:
            bot.send_message(id, f"An error occured. Try choosing a different format.")
    shutil.rmtree(chat_folder)