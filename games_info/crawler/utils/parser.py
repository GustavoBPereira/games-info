from bs4 import BeautifulSoup


class Parser:

    def steam_data(self, data):
        return {
            'type': data['type'],
            'game_name': data['name'],
            'is_free': data['is_free'],
            'short_description': data['short_description'],
            'supported_languages': data['supported_languages'],
            'price_overview': data.get('price_overview'),
            'platforms': data['platforms'],
            'metacritic': data.get('metacritic', {}),
            'genres': data['genres'],
            'recommendations': data.get('recommendations', {}).get('total'),
            'release_date': data['release_date'],
            'header_image': data['header_image'],
            'background_image': data.get('screenshots', [{}])[0].get('path_full', None)
        }
    
    
    def how_long_data(self, data):
        html = data.text

        soup = BeautifulSoup(html, 'html.parser')

        try:
            how_long_data = soup.find('div', {'class': 'search_list_details_block'})
            titles = [title.text for title in how_long_data.find_all('div', {'class': 'shadow_text'})]
            hours = [hour.text for hour in how_long_data.find_all('div', {'class': 'center'})]
        except AttributeError:
            return [['Time information not find', '']]

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
