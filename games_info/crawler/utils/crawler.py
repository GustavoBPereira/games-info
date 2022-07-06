import requests

from games_info.crawler import accepted_currency, headers
from games_info.crawler.exceptions import TypeNotSupported
from games_info.crawler.utils import Parser


class Crawler(Parser):
    steam_api_url = 'http://store.steampowered.com/api'

    def __init__(self, app_id, currency='us'):
        self.currency = currency if currency in list(accepted_currency.keys()) else 'us'
        self.language = accepted_currency[self.currency]["language"]
        self.app_id = app_id

    def get_data_from_steamdb(self):
        req = requests.get(f'{self.steam_api_url}/appdetails?appids={self.app_id}&cc={self.currency}&l={self.language}')
        json_response = req.json()[self.app_id]['data']
        if json_response['type'].lower() not in ['game', 'dlc']:
            raise TypeNotSupported(
                f'steam crawler only supports game and dlc, type finded is: {json_response["type"].lower()}')
        return self.steam_data(json_response)

    def get_data_from_how_long(self, real_game_name):
        how_long_headers = headers
        how_long_headers['referer'] = 'https://howlongtobeat.com'
        session = requests.Session()
        req = session.post('https://howlongtobeat.com/search_results?page=1', headers=how_long_headers, data={
            'queryString': real_game_name.replace('™', '').replace('®', ''),
            't': 'games',
            'sorthead': 'popular',
        })
        req.raise_for_status()
        return self.how_long_data(req)

    def get_data(self):
        data = {}
        stemdb_datas = self.get_data_from_steamdb()
        how_long_datas = self.get_data_from_how_long(stemdb_datas['game_name'])

        data['steamdb'] = stemdb_datas
        data['how_long'] = how_long_datas
        return data
