import json
import os

import requests
from dotenv import load_dotenv

# Load environment variables and set paths
load_dotenv()
credentials_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'credentials.json'
)


def load_credentials():
    if os.path.exists(credentials_path):
        with open(credentials_path, 'r') as f:
            data = json.load(f)
    else:
        data = {}

    login = data.get('LOGIN') or os.getenv('LOGIN')
    password = data.get('PASSWORD') or os.getenv('PASSWORD')
    telegram_token = data.get('TELEGRAM_BOT_TOKEN') or os.getenv(
        'TELEGRAM_BOT_TOKEN'
    )

    return login, password, telegram_token


LOGIN, PASSWORD, TELEGRAM_TOKEN = load_credentials()


def check_credentials():
    global LOGIN, PASSWORD, TELEGRAM_TOKEN

    data_json = {}
    if not os.path.exists(credentials_path):
        data_json = {
            'LOGIN': '',
            'PASSWORD': '',
            'AURORA_TOKEN': '',
            'TELEGRAM_BOT_TOKEN': '',
        }
        with open(credentials_path, 'w') as loop_one:
            json.dump(data_json, loop_one, indent=2)

    while not TELEGRAM_TOKEN:
        with open(credentials_path, 'r') as loop_zero:
            data_json = json.load(loop_zero)
            TELEGRAM_TOKEN = data_json.get('TELEGRAM_BOT_TOKEN')
        if not TELEGRAM_TOKEN:
            TELEGRAM_TOKEN = input('Enter your Telegram bot token: ')
            data_json['TELEGRAM_BOT_TOKEN'] = TELEGRAM_TOKEN
            with open(credentials_path, 'w') as loop_two:
                json.dump(data_json, loop_two, indent=2)

    while not LOGIN or not PASSWORD:
        with open(credentials_path, 'r') as loop_two:
            data_json = json.load(loop_two)
            LOGIN = data_json.get('LOGIN')
            PASSWORD = data_json.get('PASSWORD')
        if not LOGIN or not PASSWORD:
            LOGIN = input('Enter your Aurora login: ')
            PASSWORD = input('Enter your Aurora password: ')
            data_json['LOGIN'] = LOGIN
            data_json['PASSWORD'] = PASSWORD
            with open(credentials_path, 'w') as loop_three:
                json.dump(data_json, loop_three, indent=2)

        check_status = requests.post(
            'https://aurorabot.net/api/v2/user/login',
            headers={'username': LOGIN, 'password': PASSWORD},
        )
        if check_status.status_code == 401:
            print('Login or password is incorrect, please try again.')
            LOGIN = ''
            PASSWORD = ''

    return True
