import json
import sys

import requests
import os

url = 'http://api.steampowered.com/ISteamApps/GetAppList/v0001/'

headers = {
    'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'
        ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    'Accept':
        'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
}


def json_file():
    return f'{os.path.dirname(os.path.abspath(__file__))}/app_ids.json'


def download():
    print('Downloading app_ids json...')
    session = requests.Session()
    req = session.get(url, headers=headers)
    with open(json_file(), 'w') as f:
        json.dump(req.json(), f, ensure_ascii=False)
    print('Done!')


def check_quantity():
    with open(json_file(), 'r') as f:
        str_file = f.read()

    json_data = json.loads(str_file)
    q = 0
    for app in json_data['applist']['apps']['app']:
        q += 1
    print(f'The quantity of app_ids in {json_file()} is: {q}')


if __name__ == '__main__':
    if '--download' in sys.argv:
        download()

    if '--check-quantity' in sys.argv:
        try:
            check_quantity()
        except FileNotFoundError:
            answer = input('Json does not exists... type yes to download: ')
            if answer.lower() == 'yes':
                download()
                check_quantity()
