import json
import os

import requests

from settings.config import (
    check_credentials,
    credentials_path,
    load_credentials,
)


def get_credentials():
    """
    Get credentials from credentials.json file.
    :return: A dictionary with credentials.
    """
    if os.path.exists(credentials_path):
        with open(credentials_path, 'r') as f:
            data = json.load(f)
        return data


def get_headers():
    """
    Get headers for Aurora API.
    :return: A dictionary with headers.
    """
    AURORA_TOKEN = get_credentials().get('AURORA_TOKEN')
    return {'Authorization': f'Bearer {AURORA_TOKEN}'}


def update_aurora_token():
    """
    Update Aurora token.
    :return: A new Aurora token.
    """
    AURORA_TOKEN = get_credentials().get('AURORA_TOKEN')

    if check_credentials():
        account_info = requests.get(
            'https://aurorabot.net/api/v2/license/summary',
            headers=get_headers(),
        )
        if account_info.status_code == 401:
            LOGIN, PASSWORD = load_credentials()[:2]
            AURORA_TOKEN = (
                requests.post(
                    'https://aurorabot.net/api/v2/user/login',
                    headers={'username': LOGIN, 'password': PASSWORD},
                )
                .json()
                .get('token')
            )
            with open(credentials_path, 'r') as f:
                data = json.load(f)

            data['AURORA_TOKEN'] = AURORA_TOKEN

            with open(credentials_path, 'w') as f:
                json.dump(data, f, indent=2)
        return AURORA_TOKEN
    else:
        return update_aurora_token()
