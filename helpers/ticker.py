"""
Ticker module allow you to get some information about a given cryptocurrency
"""
from datetime import datetime
import requests
from api.api import Api


class Ticker(Api):
    """
    This class contains some ticker helpers functions
    """""
    currency_1 = "btc"
    currency_2 = "usd"
    currency_information = {
        "actual_price": 0,
        "lowest_price": 0,
        "highest_price": 0,
        "currency": "USD",
        "date": None
    }

    def __init__(self, currency_1, currency_2):
        self.currency_1 = currency_1
        self.currency_2 = currency_2

    def get_currency_information(self):
        """
        :return: Return formatted currency / USD information
        :rtype: dict
        """
        response = requests.get(
            self.get_full_endpoint(f"/pubticker/{self.currency_1}{self.currency_2}")
        ).json()

        self.currency_information.update({
            "actual_price": round(float(response["last_price"])),
            "lowest_price": round(float(response["low"])),
            "highest_price": round(float(response["high"])),
            "date": datetime.fromtimestamp(float(response["timestamp"]))
        })

        print(self.currency_information)
