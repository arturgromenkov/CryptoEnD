from abc import ABC, abstractmethod
from utils import get_keys
import time


class TradeBot(ABC):
    def __init__(self, api_key, api_secret, box, playbox=True):
        print("Bot started initializing")
        self.api_key = api_key
        self.api_secret = api_secret
        self.box = box
        self.playbox = playbox
        print(f"Bot initialized successfully - playbox:{self.playbox} at time {time.time()}")

    @abstractmethod
    def run(self):
        pass


class BasicBot(TradeBot):
    def __init__(self, api_key, api_secret, box):
        super().__init__(api_key, api_secret, box)

    def run(self):
        self.box.run()
