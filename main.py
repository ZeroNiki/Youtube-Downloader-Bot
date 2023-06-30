import yt_dlp as ytd
from aiogram import Dispatcher, Bot, executor, types
from aiogram import asyncio
from aiogram.dispatcher.filters import Text
from config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher(bot)

# Начало
@dp.message_handler(commands='start')
async def hello(message: types.Message):
    start_button = ['Установить']
    keyboards = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboards.add(*start_button)
    await message.answer("Привет! Это бот установщик видео с youtube", reply_markup=keyboards)

# Установить
@dp.message_handler(Text(equals='Установить'))
async def start_dw(message: types.Message):
    await message.reply('Скинь ссылку!')

@dp.message_handler(content_types='text')
async def downloading(message: types.Message):
    link = message.text

    options = {'skip-download': True, 'format': 'mp4'}

    with ytd.YoutubeDL(options) as ytdl:
        ytdl.download([link])
        result = ytdl.extract_info("{}".format(link))
        title = ytdl.prepare_filename(result)
        video = open(f'{title}', 'rb')
        await bot.send_video(message.chat.id, video=video)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

