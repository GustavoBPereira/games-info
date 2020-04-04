from selenium import webdriver
from bs4 import BeautifulSoup

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GameCrawler:
    def __init__(self, game_name):
        self.driver = webdriver.Chrome()
        self.game_name = game_name

    def get_data_from_steamdb(self):
        self.driver.get(f"https://steamdb.info/instantsearch/?query={self.game_name.replace(' ', '+')}")
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_class_name('s-hit').click()

        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        real_name = soup.find('h1').text
        prices = soup.find('td', {'data-cc': 'br'})
        current_price = prices.next_sibling.next_sibling.text
        best_price = prices.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.text
        return {'real_name': real_name, 'current_price': current_price, 'best_price': best_price}

    def get_data_from_how_long(self, real_game_name):

        self.driver.get("https://howlongtobeat.com/")
        elem = self.driver.find_element_by_name("global_search_box")
        elem.clear()
        elem.send_keys(real_game_name)

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'search_list_details_block')))

        soup = BeautifulSoup(self.driver.page_source, 'html.parser')

        how_long_data = soup.find('div', {'class': 'search_list_details_block'})

        titles = [title.text for title in how_long_data.find_all('div', {'class': 'shadow_text'})]
        hours = [hour.text for hour in how_long_data.find_all('div', {'class': 'time_100'})]

        time_data = {}
        for title in titles:
            for hour in hours:
                cleaned_hour = hour.strip()
                if '½' in cleaned_hour:
                    cleaned_hour = hour.replace('½', '')
                    cleaned_hour += ' 30 Mins'
                time_data[title] = cleaned_hour
                hours.remove(hour)
                break
        return time_data

    def get_data(self):
        data = {}
        stemdb_datas = self.get_data_from_steamdb()
        how_long_datas = self.get_data_from_how_long(stemdb_datas['real_name'])

        self.close()

        data['steamdb'] = stemdb_datas
        data['how_long'] = how_long_datas
        return data

    def close(self):
        self.driver.quit()
