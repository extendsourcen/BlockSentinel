from blocksentinel.monitor import WalletMonitor
from blocksentinel.analyzer import TransactionAnalyzer
from blocksentinel.risk_engine import RiskEngine
from dotenv import load_dotenv
import os
import json

# Load environment variables
load_dotenv()

def main():
    wallet_address = input("Enter Ethereum wallet address: ")

    monitor = WalletMonitor()
    transactions = monitor.get_transactions(wallet_address)

    analyzer = TransactionAnalyzer(transactions)
    analysis_result = analyzer.analyze()

    risk_engine = RiskEngine(analysis_result)
    risk_score = risk_engine.calculate_risk()

    report = {
        "wallet": wallet_address,
        "analysis": analysis_result,
        "risk_score": risk_score
    }

    with open(f"reports/{wallet_address}.json", "w") as f:
        json.dump(report, f, indent=4)

    print("\nRisk Score:", risk_score)
    print("Report saved to reports/")

if __name__ == "__main__":
    main()
