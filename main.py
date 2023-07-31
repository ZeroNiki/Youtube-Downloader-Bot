import yt_dlp as ytd
import requests
from aiogram import Dispatcher, Bot, executor, types
from aiogram import asyncio
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher.filters import Text
from config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher(bot)

# Начало


@dp.message_handler(commands='start')
async def hello(message: types.Message):
    # Обычные кнопки
    start_button = ['Установить']
    keyboards = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboards.add(*start_button)

    # Inline кнопки
    link_buttons = [
        InlineKeyboardButton(
            text='GitHub', url='https://github.com/ZeroNiki/Youtube-Downloader-Bot')
    ]
    link_keyboards = InlineKeyboardMarkup(row_width=1)
    link_keyboards.add(*link_buttons)

    await message.answer("Привет! Это бот установщик видео с youtube", reply_markup=link_keyboards)
    await message.answer("↑↑↑↑ Подпишитесь на мой github ↑↑↑↑", reply_markup=keyboards)

# Inline кнопка устоновки в формате .mp4


@dp.callback_query_handler(text='download_mp4')
async def inline_keyboard_mp4(call: types.CallbackQuery):
    options = {'skip-download': True, 'format': 'mp4',
               'outtmpl': 'video/%(title)s.%(ext)s'}

    with ytd.YoutubeDL(options) as ytdl:
        ytdl.download([link])
        result = ytdl.extract_info("{}".format(link))
        title = ytdl.prepare_filename(result)
        video = open(f'{title}', 'rb')

        await call.message.answer_video(video=video)

# Inline кнопка устоновки в формате .mp3


@dp.callback_query_handler(text='download_mp3')
async def inline_keyboard_mp3(call: types.CallbackQuery):
    options = {
        'skip-download': True,
        'format': 'bestaudio/best',
        'outtmpl': 'mp3/%(title)s.%(ext)s',
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

        await call.message.answer_audio(audio=audio)

# Установить изображение


@dp.callback_query_handler(text='download_jpg')
async def inline_keyboard_jpg(call: types.CallbackQuery):
    with ytd.YoutubeDL({}) as ytdl:
        info_dict = ytdl.extract_info(link, download=False)
        get_id = info_dict.get('id', None)

    thumbnail = f'https://img.youtube.com/vi/{get_id}/maxresdefault.jpg'
    r = requests.get(thumbnail)

    if r.status_code == 200:
        with open(f"jpg/{get_id}.jpg", "wb") as file:
            file.write(r.content)

    with open(f"jpg/{get_id}.jpg", "rb") as f:
        content = f.read()
        await call.message.answer_photo(photo=content)


# Установить
@dp.message_handler(Text(equals='Установить'))
async def start_dw(message: types.Message):
    await message.reply('Скинь ссылку!')


@dp.message_handler(content_types='text')
async def downloading(message: types.Message):
    global link
    link = message.text
    keyboard = InlineKeyboardMarkup()

    keyboard.add(
        InlineKeyboardButton(text='.mp4', callback_data='download_mp4'),
        InlineKeyboardButton(text='.mp3', callback_data='download_mp3'),
        InlineKeyboardButton(text='🖼️', callback_data='download_jpg')
    )

    await message.answer(message.text, reply_markup=keyboard)
    await message.delete()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
