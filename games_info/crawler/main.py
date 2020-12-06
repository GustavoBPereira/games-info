import requests
from bs4 import BeautifulSoup


class GameCrawler:
    accepted_currency = ['us', 'eu', 'ar', 'au', 'br', 'uk', 'ca', 'cl', 'cn', 'az', 'co', 'cr', 'hk', 'in', 'id', 'il',
                         'jp', 'kz', 'kw', 'my', 'mx', 'nz', 'no', 'pe', 'ph', 'pl', 'qa', 'ru', 'sa', 'sg', 'za', 'pk',
                         'kr', 'ch', 'tw', 'th', 'tr', 'ae', 'ua', 'uy', 'vn', ]

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)AppleWebKit 537.36 (KHTML, like Gecko) Chrome',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    }

    def __init__(self, app_id, currency='us'):
        self.currency = currency if currency in self.accepted_currency else 'us'
        self.app_id = app_id

    def get_data_from_steamdb(self):
        url = f'http://store.steampowered.com/api/appdetails?appids={self.app_id}&cc={self.currency}&l={self.currency}'
        req = requests.get(url)
        data = req.json()[self.app_id]['data']
        return {'game_name': data['name'], 'price': data['price_overview']}

    def get_data_from_how_long(self, real_game_name):
        session = requests.Session()
        url = 'https://howlongtobeat.com/search_results?page=1'
        req = session.post(url, headers=self.headers, data={
            'queryString': real_game_name,
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
        how_long_datas = self.get_data_from_how_long(stemdb_datas['real_name'])

        data['steamdb'] = stemdb_datas
        data['how_long'] = how_long_datas
        return data
