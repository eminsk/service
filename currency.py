from bs4 import BeautifulSoup
import requests

class CurrencyChecker:
    """ Класс для проверки курса валют """

    def __init__(self):
        self.urls = {
            'USD_RUB': 'https://www.google.com/search?q=доллар+российской+рубль',
            'USD_BYN': 'https://www.google.com/search?q=доллар+белорусский+рубль',
            'BYN_RUB': 'https://www.google.com/search?q=белорусский+рубль+в+российской+рубль',
        }

    def get_currency_rate(self, url):
        response = requests.get(url, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/237.84.2.178 Safari/537.36'
        })
        soup = BeautifulSoup(response.text, 'lxml')
        rate_element = soup.find('span', class_='SwHCTb')
        if rate_element:
            return rate_element.text.strip()

    def check_currency(self):
        rates = {}
        for currency, url in self.urls.items():
            rate = self.get_currency_rate(url)
            if rate:
                rates[currency] = rate
            else:
                print(f'Не удалось получить курс для {currency}.')

        return rates