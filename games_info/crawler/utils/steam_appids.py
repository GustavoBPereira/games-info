import requests

from games_info.crawler import headers

url = 'http://api.steampowered.com/ISteamApps/GetAppList/v0001/'

def get_app_ids():
    session = requests.Session()
    req = session.get(url, headers=headers)
    req.raise_for_status()
    return req.json()
