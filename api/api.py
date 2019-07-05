"""
API module contain all the connection and Bitfinex API relation
"""
class Api:
    """
    API helper functions
    """
    url = "https://api.bitfinex.com/v1"

    def get_full_endpoint(self, path):
        """
        :param path: str
        :return: Return the formatted API URL with the good endpoint
        :rtype: str
        """
        return self.url + path

    def get_root_endpoint(self):
        """
        :return: Return the root API URL
        :rtype: str
        """
        return self.url
