from pybit.unified_trading import WebSocket
from pybit.unified_trading import HTTP
import time
import configparser


def get_keys(net='RealNet'):
    config = configparser.ConfigParser()
    config.read('/home/artur/PycharmProjects/Crypto_bot/config.ini')
    return config[net]['api_key'], config[net]['api_secret']

kek = []

def handle_message(m):
    print(m)
#    print(m['data'])
def handle_kline(m):
    kek.append(m['data'])


class Connector:
    def __init__(self, api_key, api_secret):
        self.ws = WebSocket(
            testnet=True,
            channel_type="linear",
            api_key=api_key,
            api_secret=api_secret,
            callback_function=handle_message
        )

    def run(self):
        # self.ws.wallet_stream(callback=handle_message)
        self.ws.ticker_stream(callback=handle_message, symbol="BTCUSDT") # linear
        # self.ws.execution_stream(callback=handle_message)
        # self.ws.orderbook_stream(callback=handle_message, depth=1, symbol="BTCUSDT") # linear
        # self.ws.position_stream(callback=handle_message)
        # self.ws.kline_stream(callback=handle_message, interval="1", symbol=["BTCUSDT","ETHUSDT"])
        # self.ws.lt_kline_stream(callback=handle_message)

        while True:
            time.sleep(1)


# api_key, api_secret = get_keys()
# Connector = Connector(api_key, api_secret)
# Connector.run()

class KlineConnection:
    def __init__(self, api_key, api_secret):
        self.ws = WebSocket(
            testnet=False,
            channel_type="linear",
            api_key=api_key,
            api_secret=api_secret,
            callback_function=handle_message
        )

    def run(self,symbols,interval='1'):
        responce = self.ws.kline_stream(interval=interval, symbol=symbols, callback=handle_kline)
        print(responce)

api_key, api_secret = get_keys()
connector = KlineConnection(api_key, api_secret)
connector.run(['BTCUSDT'])
while True:
    print(kek)