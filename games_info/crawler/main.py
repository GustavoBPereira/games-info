from selenium import webdriver
from bs4 import BeautifulSoup


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

    def close(self):
        self.driver.quit()
