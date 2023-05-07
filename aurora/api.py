import logging
from pprint import pprint

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


def get_extented_info():
    full_info = get_full_info()
    if full_info is None:
        return None

    list_more_than_25 = []
    list_less_than_25 = []
    list_more_than_50000 = []
    list_more_than_30000 = []
    list_region_ru_in_game = []
    list_region_euw_in_game = []
    # server_bot_counts = {}
    # unnamed_server = 'Unnamed Server'

    for account in full_info:
        if account['level'] >= 25:
            list_more_than_25.append(account)
        elif 25 >= account['level'] >= 1:
            list_less_than_25.append(account)

        if account['blue_essence'] >= 50000:
            list_more_than_50000.append(account)
        elif account['blue_essence'] >= 30000:
            list_more_than_30000.append(account)

        if account['region'] == 'RU' and account['in_game'] == 1:
            list_region_ru_in_game.append(account)
        elif account['region'] == 'EUW' and account['in_game'] == 1:
            list_region_euw_in_game.append(account)

        # if account['in_game'] == 1:
        #     server = account['server_name']
        #     if server is None:
        #         server = unnamed_server
        #
        #     if server not in server_bot_counts:
        #         server_bot_counts[server] = 0
        #     server_bot_counts[server] += 1

    final_dict = {
        'more_than_25': len(list_more_than_25),
        'less_than_25': len(list_less_than_25),
        'more_than_50000': len(list_more_than_50000),
        'more_than_30000': len(list_more_than_30000),
        'region_ru_in_game': len(list_region_ru_in_game),
        'region_euw_in_game': len(list_region_euw_in_game),
        # 'server_bot_counts': server_bot_counts,
    }
    return final_dict


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
        licenses = get_valid_licenses()
        info = get_bots_status()
        banned = get_banned()
        extented_info = get_extented_info()
        running = info.get('running')
        in_game = info.get('in_game')
        fresh = info.get('fresh')
        finished = info.get('finish')
        # servers = extented_info.get('server_bot_counts')
        licenses_valid = licenses.get('valid')
        licenses_in_use = licenses.get('in_use')
        more_than_25 = extented_info.get('more_than_25')
        less_than_25 = extented_info.get('less_than_25')
        more_than_50000 = extented_info.get('more_than_50000')
        more_than_30000 = extented_info.get('more_than_30000')
        region_ru_in_game = extented_info.get('region_ru_in_game')
        region_euw_in_game = extented_info.get('region_euw_in_game')
        logging.info('Successfully fetched bots status.')
    except Exception as e:
        print(e)
        logging.error(e)
        return None

    message_text = (
        f'🪪<b>Information about licenses:</b>\n'
        f'Total licenses: <code>{licenses_valid}</code>\n'
        f'Licenses in use: <code>{licenses_in_use}</code>\n\n'
        f'🤖<b>Information about bots:</b>\n'
        f'Bots running: <code>{running}</code>\n'
        f'Bots in game: <code>{in_game}</code>\n'
        # f'Servers: <code>{servers}</code>\n\n'
        f'RU in game: <code>{region_ru_in_game}</code>\n'
        f'EUW in game: <code>{region_euw_in_game}</code>\n\n'
        f'💎<b>Information about accounts:</b>\n'
        f'Fresh accounts: <code>{fresh}</code>\n'
        f'Finished accounts: <code>{finished}</code>\n'
        f'Banned accounts: <code>{banned}</code>\n'
        f'More than 25 level: <code>{more_than_25}</code>\n'
        f'Less than 25 level: <code>{less_than_25}</code>\n'
        f'More than 50000 BE: <code>{more_than_50000}</code>\n'
        f'More than 30000 BE: <code>{more_than_30000}</code>\n'

    )
    return message_text