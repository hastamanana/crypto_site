import requests
from bs4 import BeautifulSoup
import lxml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



url = 'https://ru.investing.com/news/cryptocurrency-news'
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
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'news-analysis-v2_content__z0iLP')))
        titles = self.driver.find_elements(By.CLASS_NAME, 'news-analysis-v2_content__z0iLP')
        return titles
    
    def print_titles(self):
        all_headers = []
        for title in self.parse():
            res = [line for line in title.text.strip().split('\n') if line.strip()]
            if res:
                all_headers.append(res[0])
        return all_headers

def main_inv():
    with WebDriver(driver=driver, url=url) as wd:
        return wd.print_titles()


if __name__ == '__main__':
    try:
        main_inv()
    except Exception as e:
        print(e)
    














# class Parse:

#     headers = {
#     "User-Agent": (
#         "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
#         "AppleWebKit/537.36 (KHTML, like Gecko) "
#         "Chrome/122.0.0.0 Safari/537.36"
#     ),
#     "Referer": "https://ru.tradingview.com/news-flow/?market=crypto/",
#     "Accept-Language": "ru-RU,ru;q=0.9,en;q=0.8",
#     }


#     def __init__(self, url):
#         self.url = url
#         self.session = requests.Session()
#         self.session.headers.update(Parse.headers)

#     def response(self):
#         return self.session.get(self.url)
    
#     def get_full_html(self):
#         return BeautifulSoup(self.response().text, 'lxml')
    
#     def soup_all_headers(self):
#         return self.get_full_html().find('div', class_='apply-overflow-tooltip apply-overflow-tooltip--direction_both block-bETdSLzM title-HY0D0owe title-DmjQR0Aa').text
    
#     def parse_headers_only(self):
#         for i in self.soup_all_headers():
#             print(i.text)
        

# if __name__ == "__main__":
#     investing = Parse('https://ru.tradingview.com/news-flow/?market=crypto')
#     print(investing.soup_all_headers())

