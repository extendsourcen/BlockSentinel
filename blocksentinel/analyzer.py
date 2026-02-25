class TransactionAnalyzer:
    def __init__(self, transactions):
        self.transactions = transactions

    def analyze(self):
        """
        Perform basic transaction analysis.
        """
        total_in = 0
        total_out = 0
        tx_count = len(self.transactions)

        for tx in self.transactions:
            value = int(tx["value"]) / 10**18

            if tx["to"] is None:
                continue

            if tx["to"].lower() == tx["from"].lower():
                continue

            if tx["to"]:
                total_out += value
            else:
                total_in += value

        return {
            "transaction_count": tx_count,
            "total_out_eth": total_out,
            "total_in_eth": total_in
        }
