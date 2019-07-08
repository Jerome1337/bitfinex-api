"""
Symbols module allow you to get every currencies pairs available
"""
import requests
from api.api import Api


class Symbols(Api):
    """
    The Symbols class return information about all Bitfinex available symbols
    """
    pairs = []

    def get_pairs(self):
        """
        :return: Return all available pairs formatted
        :rtype: list
        """
        pairs = requests.get(
            self.get_full_endpoint("/symbols_details")
        ).json()

        for pair in pairs:
            self.pairs.append(pair['pair'])

        print(self.pairs)

        return self.pairs
