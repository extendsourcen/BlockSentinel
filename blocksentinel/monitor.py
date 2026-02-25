import requests
import os

class WalletMonitor:
    def __init__(self):
        self.api_key = os.getenv("ETHERSCAN_API_KEY")
        self.base_url = "https://api.etherscan.io/api"

    def get_transactions(self, address):
        """
        Fetch transactions for a given Ethereum address using Etherscan API.
        """
        params = {
            "module": "account",
            "action": "txlist",
            "address": address,
            "startblock": 0,
            "endblock": 99999999,
            "sort": "asc",
            "apikey": self.api_key
        }

        response = requests.get(self.base_url, params=params)
        data = response.json()

        if data["status"] != "1":
            return []

        return data["result"]
