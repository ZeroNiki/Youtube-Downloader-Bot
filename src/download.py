import src.keyboards as kb

from aiogram import Router, F, types
from aiogram.types import Message, CallbackQuery, FSInputFile
# from aiogram.methods import SendVideo, SendAudio, SendPhoto

import yt_dlp as ytd
import wget
import os
import shutil

rt = Router()


@rt.message(F.text)
async def getLink(message: Message):
    global link
    link = message.text

    await message.answer(message.text, reply_markup=kb.chBtn)
    await message.delete()


@rt.callback_query(F.data == "1080")
async def dw_1080(callback: CallbackQuery):
    await callback.message.answer("...")

    options = {
        'skip-download': True,
        'format_sort': ['res:1080', 'ext:mp4:m4a'],
        'outtmpl': 'output/video/%(title)s.%(ext)s'
    }

    with ytd.YoutubeDL(options) as ytdl:
        ytdl.download([link])
        result = ytdl.extract_info("{}".format(link))
        title = ytdl.prepare_filename(result)
        video = open(f'{title}', 'rb')

        await callback.message.answer_video(FSInputFile(path=video.name))

        folder = 'output/video/'
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)

            except Exception as e:
                print('Error %s. Reason: %s' % (file_path, e))


@rt.callback_query(F.data == "720")
async def dw_720(callback: CallbackQuery):
    await callback.message.answer("...")
    options = {
        'skip-download': True,
        'format_sort': ['res:720', 'ext:mp4:m4a'],
        'outtmpl': 'output/video/%(title)s.%(ext)s'
    }

    with ytd.YoutubeDL(options) as ytdl:
        ytdl.download([link])
        result = ytdl.extract_info("{}".format(link))
        title = ytdl.prepare_filename(result)
        video = open(f'{title}', 'rb')

        await callback.message.answer_video(FSInputFile(path=video.name))

        folder = 'output/video/'

        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)

            except Exception as e:
                print('Error %s. Reason: %s' % (file_path, e))


@rt.callback_query(F.data == "360")
async def dw_360(callback: CallbackQuery):
    await callback.message.answer("...")

    options = {
        'skip-download': True,
        'format_sort': ['res:360', 'ext:mp4:m4a'],
        'outtmpl': 'output/video/%(title)s.%(ext)s'
    }

    with ytd.YoutubeDL(options) as ytdl:
        ytdl.download([link])
        result = ytdl.extract_info("{}".format(link))
        title = ytdl.prepare_filename(result)
        video = open(f"{title}", 'rb')

        await callback.message.answer_video(FSInputFile(path=video.name))

        folder = 'output/video/'

        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)

            except Exception as e:
                print('Error %s. Reason: %s' % (file_path, e))


@rt.callback_query(F.data == "mp3")
async def dw_mp3(callback: CallbackQuery):
    await callback.message.answer("...")

    options = {
        'skip-download': True,
        'format': 'bestaudio/best',
        'outtmpl': 'output/mp3/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with ytd.YoutubeDL(options) as ytdl:
        ytdl.download([link])
        result = ytdl.extract_info("{}".format(link))
        title = ytdl.prepare_filename(result)[:-5]
        audio = open(f'{title}.mp3', 'rb')

        await callback.message.answer_audio(FSInputFile(path=audio.name))

    folder = 'output/mp3/'

    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)

        except Exception as e:
            print('Error %s. Reason: %s' % (file_path, e))


@rt.callback_query(F.data == "jpg")
async def dw_jpg(callback: CallbackQuery):
    await callback.message.answer("...")

    with ytd.YoutubeDL({}) as ytdl:
        info_dict = ytdl.extract_info(link, download=False)
        get_id = info_dict.get('id', None)

    thumbnail = f'https://img.youtube.com/vi/{get_id}/maxresdefault.jpg'

    wget.download(thumbnail, out="output/jpg/thumb.jpg")

    await callback.message.answer_photo(FSInputFile(path="output/jpg/thumb.jpg"))

    folder = 'output/jpg/'

    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)

        except Exception as e:
            print('Error %s. Reason: %s' % (file_path, e))
