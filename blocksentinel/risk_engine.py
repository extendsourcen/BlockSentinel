class RiskEngine:
    def __init__(self, analysis):
        self.analysis = analysis

    def calculate_risk(self):
        """
        Calculate a simple heuristic-based risk score.
        """
        score = 0

        # High transaction count may indicate bot activity
        if self.analysis["transaction_count"] > 500:
            score += 30

        # Large outgoing volume
        if self.analysis["total_out_eth"] > 100:
            score += 40

        # Low inbound but high outbound pattern
        if self.analysis["total_in_eth"] < 1 and self.analysis["total_out_eth"] > 50:
            score += 30

        return min(score, 100)
