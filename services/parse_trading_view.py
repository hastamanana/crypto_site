import time

import requests
from bs4 import BeautifulSoup
import lxml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



url = 'https://ru.tradingview.com/news-flow/?market=crypto'
driver = webdriver.Chrome()

class WebDriver:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.quit()

    def parse(self):
        self.driver.get(self.url)
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'article.article-e0sK1tJv')))
        titles = self.driver.find_elements(By.CSS_SELECTOR, 'article.article-e0sK1tJv')
        return titles
    
    def print_titles(self):
        all_headers = []
        for title in self.parse():
            res = title.text.strip().split('\n')
            all_headers.append(res[1])
        return all_headers


def main_tv():
    with WebDriver(driver=driver, url=url) as wd:
        return wd.print_titles()


if __name__ == '__main__':
    try:
        main_tv()
    except Exception as e:
        print(e)
    
