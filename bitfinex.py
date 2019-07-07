"""
Main ticker script
"""
from time import sleep
from tickers.bitcoin import Bitcoin

TICKER = Bitcoin()

while True:
    TICKER.get_bitcoin_information()
    sleep(20)
