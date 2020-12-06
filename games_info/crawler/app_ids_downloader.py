import json
import requests
import os

url = 'http://api.steampowered.com/ISteamApps/GetAppList/v0001/'

session = requests.Session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}

req = session.get(url, headers=headers)

CRAWLER_FOLDER = os.path.dirname(os.path.abspath(__file__))
with open(f'{CRAWLER_FOLDER}/app_ids.json', 'w') as f:
    json.dump(req.json(), f, ensure_ascii=False)

