"""
Bitcoin file part of the tickets module
"""
from datetime import datetime
import requests
from api.api import Api


class Bitcoin(Api):
    """
    This class contains some helpers functions about Bitcoin
    """
    bitcoin_information = {
        "actual_price": 0,
        "lowest_price": 0,
        "highest_price": 0,
        "currency": "US Dollar",
        "date": None
    }

    def get_bitcoin_information(self):
        """
        :return: Return formatted Bitcoin / USD information
        :rtype: dict
        """
        response = requests.get(self.get_full_endpoint("/pubticker/btcusd")).json()

        self.bitcoin_information.update({
            "actual_price": round(float(response["last_price"])),
            "lowest_price": round(float(response["low"])),
            "highest_price": round(float(response["high"])),
            "date": datetime.fromtimestamp(float(response["timestamp"]))
        })

        print(self.bitcoin_information)
