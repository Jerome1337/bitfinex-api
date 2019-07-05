from time import sleep
from tickers.bitcoin import Bitcoin

ticker = Bitcoin()

while True:
    ticker.get_bitcoin_information()
    sleep(20)
