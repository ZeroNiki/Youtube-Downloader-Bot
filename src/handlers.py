import src.keyboards as kb

from aiogram import F, Router, html
from aiogram.filters import CommandStart, Command 
from aiogram.types import Message

router = Router()

@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.reply(f"Hi, {html.bold(message.from_user.full_name)}!", reply_markup=kb.main)
    await message.answer("Give the github repository a star", reply_markup=kb.gitBtn)


@router.message(F.text == "Install")
async def replyMsg(message: Message):
    await message.reply("Send a link to the YouTube video you want to download")




