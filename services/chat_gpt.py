import requests
import json
from functools import lru_cache

from .parse_investing import main_inv
from .parse_trading_view import main_tv
from .price_token import get_btc_price, get_eth_price

from environs import Env


class Predict_price:

    
   

    """
    Класс для прогнозирования цены BTC + ETH на основе заголовков мировых новостей.

    Класс использует OpenAI API для предсказывания цены на биткоин и эфир.

    Attributes:
        client: Объект клиента OpenAI, инициализируется с помощью API токена.
        description (str): Инструкция для прогнозирования цен.
        news_headers_investing (str): Заголовки новостей с сайта `investing`.
        news_headers_trading_view (str): Заголовки новостей с сайта `trading view`.
    """
    @classmethod
    def get_token(cls):
        env = Env()
        env.read_env()
        return env('API_TOKEN')


    btc_price = get_btc_price()
    eth_price = get_eth_price()

    client = None
    description = f"""
                    Ты аналитик криптовалют. На вход получаешь список новостных заголовков по BTC и ETH.
                    На основе их дай прогноз движения цены BTC и ETH на неделю, месяц и полгода.
                    Используй только следующие символы стрелок , то есть куда пойдет цена относительно текущего курса: ↑ (вверх), ↓ (вниз), → (без изменений).
                    Текущая цена BTC: {btc_price}
                    Текущая цена BTC: {eth_price}
                    Пример правильного JSON-ответа:

                    {{
                    "week": {{"btc": "↑ $ 110,590.85", "eth": "↓ $ 2,105.85"}},
                    "month": {{"btc": "↓ $ 102,480.85", "eth": "↑ $ 3,390.85"}},
                    "six_months": {{"btc": "→ $ 105,800.85", "eth": "↑ $ 5,900.85"}}
                    }}

                    Отвечай строго в таком формате без лишнего текста.
                    """

    def __init__(self, news_headers_investing, news_headers_trading_view) -> None:
        """
        Инициализация объекта класса Predict_price.

        Args:
            news_headers_investing: Заголовки крипто-новостей c сайта `investing`.
            news_headers_trading_view: Заголовки крипто-новостей c сайта`trading view`.
        """
        token = Predict_price.get_token()
        self.news_headers_investing = news_headers_investing
        self.news_headers_trading_view = news_headers_trading_view


class Predict_priceThisOutOfOpenAI(Predict_price):
    """
    Класс для прогнозирования цены BTC + ETH на основе заголовков мировых новостей.
в
    Класс наследуется от класса Predict_price и использует OpenAI API для прогнозирования цены BTC + ETH на основе заголовков мировых новостей.
    Не использует библиотеку OpenAI.
    """

    def __init__(self, news_headers_investing, news_headers_trading_view) -> None:
        """
        Инициализация объекта класса Predict_priceThisOutOfOpenAI.

        Args:
            news_headers_investing: Заголовки крипто-новостей c сайта `investing`.
            news_headers_trading_view: Заголовки крипто-новостей c сайта`trading view`.
        """
        self.token = Predict_price.get_token()
        super().__init__(news_headers_investing, news_headers_trading_view)

    def get_response(self) -> str:
        """
        Выполняет запрос к OpenAI API для прогнозирования цены BTC + ETH на основе заголовков мировых новостей.

        Формирует запрос к модели с инструкцией.

        Returns:
            json: Цены на биткоин и эфир, сгенерированные OpenAI.
        """
        user_request = (f'Заголовки: {'. '.join(self.news_headers_investing)}. {'. '.join(self.news_headers_trading_view)}')

        # Заголовки запроса
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.token}'
        }

        # Данные запроса
        data = {
            "model": "gpt-4.1-mini",  # Или другой доступный вам вариант модели
            "messages": [
                {"role": "system", "content": self.description},
                {"role": "user", "content": user_request}
            ],
            "max_tokens": 250,
            "temperature": 0.8
        }

        # Отправка POST-запроса к API
        response = requests.post(
            'https://api.proxyapi.ru/openai/v1/chat/completions',
            headers=headers, data=json.dumps(data))

        # Обработка ответа
        if response.status_code == 200:
            result = response.json()
            return result['choices'][0]['message']['content']
        else:
            return f"Error: {response.status_code}\n{response.text}"
        
@lru_cache
def main():
    crypto_news = Predict_priceThisOutOfOpenAI(news_headers_investing=main_inv(), news_headers_trading_view=main_tv())
    res =  crypto_news.get_response()
    res_json = json.loads(res)
    print(res_json)
    return res_json

if __name__ == '__main__':
    main()
