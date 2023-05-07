import logging

import requests

from aurora.token import get_headers, update_aurora_token

token = update_aurora_token()


def get_bots_status():
    """
    Fetch bots status information from the Aurora API.
    :return: A list of bots status.
    """
    try:
        summary = requests.get(
            'https://aurorabot.net/api/v2/leagueaccount/summary',
            headers=get_headers(),
        )
        logging.info('Successfully fetched bots summary information.')
    except Exception as e:
        print(e)
        logging.error(e)
        return None

    return summary.json()


def get_valid_licenses():
    """
    Fetch valid licenses summary information from the Aurora API.
    :return: A list of valid licenses.
    """
    try:
        license_info = requests.get(
            'https://aurorabot.net/api/v2/license/summary',
            headers=get_headers(),
        )
        logging.info('Successfully fetched license summary information.')
    except Exception as e:
        print(e)
        logging.error(e)
        return None
    return license_info.json()


def get_full_info():
    """
    Fetch full account information from the Aurora API.
    :return: A list of all accounts.
    """
    try:
        full_info = requests.get(
            'https://aurorabot.net/api/v2/leagueaccount',
            headers=get_headers(),
        )
        logging.info('Successfully fetched full account information.')
    except Exception as e:
        print(e)
        logging.error(e)
        return None
    return full_info.json()


def get_banned():
    """
    Fetch banned accounts from the Aurora API.
    :return: The number of banned accounts.
    """
    try:
        banned = requests.get(
        'https://aurorabot.net/api/v2/leagueaccount?banned=1',
        headers=get_headers(),
    )
        logging.info('Successfully fetched banned accounts.')
    except Exception as e:
        print(e)
        logging.error(e)
        return None
    return len(banned.json())


def get_running_info():
    """
    Fetch running accounts from the Aurora API and sort them by level.
    :return: A formatted list of running accounts sorted by level.
    """
    acc_list = []
    try:
        running = requests.get(
            'https://aurorabot.net/api/v2/leagueaccount?running=1',
            headers=get_headers(),
        )
        logging.info('Successfully fetched running accounts.')
    except Exception as e:
        print(e)
        logging.error(e)
        return None
    for account in running.json():
        username = account.get('username')
        region = account.get('region')
        level = int(account.get('level'))
        acc_list.append(
            {'region': region, 'level': level, 'username': username}
        )

    # Sort the account list by level in descending order
    sorted_acc_list = sorted(acc_list, key=lambda x: x['level'], reverse=True)

    # Format the sorted account list
    formatted_acc_list = [
        f"{acc['region']} | {acc['level']} | {acc['username']} \n"
        for acc in sorted_acc_list
    ]
    return formatted_acc_list


def get_message():
    """
    Get bots status and return a formatted message.
    :return:  A formatted message with bots status.
    """
    try:
        info = get_bots_status()
        banned = get_banned()
        running = info.get('running')
        in_game = info.get('in_game')
        fresh = info.get('fresh')
        finished = info.get('finish')
        logging.info('Successfully fetched bots status.')
    except Exception as e:
        print(e)
        logging.error(e)
        return None

    message_text = (
        f'Bots running: <code>{running}</code>\n'
        f'Bots in game: <code>{in_game}</code>\n'
        f'Fresh accounts: <code>{fresh}</code>\n'
        f'Finished accounts: <code>{finished}</code>\n'
        f'Banned accounts: <code>{banned}</code>'
    )
    return message_text
