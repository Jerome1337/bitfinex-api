"""
Main ticker script
"""
from time import sleep
from helpers.ticker import Ticker

TICKER = Ticker("btc", "usd")

while True:
    TICKER.get_currency_information()
    sleep(20)
