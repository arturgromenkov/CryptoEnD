import configparser
import time
import requests
from bs4 import BeautifulSoup

from pybit.unified_trading import HTTP, WebSocket

config = configparser.ConfigParser()
config.read('config.ini')

api_key = config["TestNet"]['api_key']
api_secret = config["TestNet"]['api_secret']


url = 'https://www.crypto-rating.com/crypto-currencies/'
page = requests.get(url)

print(page.status_code)
soup = BeautifulSoup(page.text, 'html.parser')
table = soup.find('table',class_='table align-middle')
print(table.tbody)
