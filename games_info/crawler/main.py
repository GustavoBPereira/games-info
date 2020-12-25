import requests
from bs4 import BeautifulSoup
from games_info.crawler import accepted_currency


class GameCrawler:

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    }

    def __init__(self, app_id, currency='us'):
        self.currency = currency if currency in list(accepted_currency.keys()) else 'us'
        self.app_id = app_id

    def get_data_from_steamdb(self):
        url = f'http://store.steampowered.com/api/appdetails?' \
              f'appids={self.app_id}&cc={self.currency}&l={accepted_currency[self.currency]["language"]}'
        req = requests.get(url)
        json_response = req.json()[self.app_id]['data']
        data = {
            'type': json_response['type'],
            'game_name': json_response['name'],
            'is_free': json_response['is_free'],
            'short_description': json_response['short_description'],
            'supported_languages': json_response['supported_languages'],
            'price_overview': json_response.get('price_overview'),
            'platforms': json_response['platforms'],
            'metacritic': json_response.get('metacritic', {}),
            'genres': json_response['genres'],
            'recommendations': json_response.get('recommendations', {}).get('total'),
            'release_date': json_response['release_date'],
            'header_image': json_response['header_image']
        }
        return data

    def get_data_from_how_long(self, real_game_name):
        session = requests.Session()
        url = 'https://howlongtobeat.com/search_results?page=1'
        req = session.post(url, headers=self.headers, data={
            'queryString': real_game_name.replace('™', ''),
            't': 'games',
            'sorthead': 'popular'
        })

        html = req.text

        soup = BeautifulSoup(html, 'html.parser')

        how_long_data = soup.find('div', {'class': 'search_list_details_block'})
        titles = [title.text for title in how_long_data.find_all('div', {'class': 'shadow_text'})]
        hours = [hour.text for hour in how_long_data.find_all('div', {'class': 'center'})]

        time_data = []
        for title in titles:
            for hour in hours:
                cleaned_hour = hour.strip()
                if '½' in cleaned_hour:
                    cleaned_hour = hour.replace('½', '')
                    cleaned_hour += '30 Mins'
                time_data.append([title, cleaned_hour])
                hours.remove(hour)
                break
        return time_data

    def get_data(self):
        data = {}
        stemdb_datas = self.get_data_from_steamdb()
        how_long_datas = self.get_data_from_how_long(stemdb_datas['game_name'])

        data['steamdb'] = stemdb_datas
        data['how_long'] = how_long_datas
        return data
