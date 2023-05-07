import logging

from aiogram import executor

from aurora.token import update_aurora_token
from telegram.bot import dp


def start_bot():
    print('Starting bot...')
    executor.start_polling(dp, skip_updates=True)


def create_token():
    print('Creating token...')
    update_aurora_token()


if __name__ == '__main__':
    # Set up logging configuration
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    )
    create_token()
    start_bot()
