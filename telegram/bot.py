import logging

import aiogram
from aiogram import types
from aiogram.dispatcher.filters import Text

from aurora.api import get_message
from settings.config import TELEGRAM_TOKEN
from telegram.keyboards import keyboard

# Initialize the bot with the Telegram token and the parse mode
bot = aiogram.Bot(token=TELEGRAM_TOKEN, parse_mode=types.ParseMode.HTML)
dp = aiogram.Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: aiogram.types.Message):
    """
    Handle the /start command and send a message with the main keyboard.
    """
    try:
        await message.answer(
            '🤖 Hello! I am glad to help you get short info '
            'about your Aurora farm.',
            reply_markup=keyboard,
        )
        logging.info('/start command processed')
    except Exception as e:
        await message.answer(f'Error: {e}')
        logging.error(e)


@dp.message_handler(Text(equals=['ℹ️Info']))
async def process_info_command(message: aiogram.types.Message):
    """
    Handle the ℹ️Info button and send a message with the current bot status.
    """
    try:
        await message.answer(get_message())
        logging.info('ℹ️Info sent')
    except Exception as e:
        await message.answer(f'Error: {e}')
        logging.error(e)
