from original.TradeBot import TradeBot
from utils import get_keys

api_key,api_secret = get_keys()
bot = TradeBot(api_key,api_secret,box=None)

bot.run()