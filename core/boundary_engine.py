class BoundaryEngine:
    """
    Determines whether an action crosses autonomy boundary.
    """

    def __init__(self):
        # threshold per domain
        self.thresholds = {
            "code": 70,
            "communication": 55,
            "system": 40,
            "finance": 25
        }

    def evaluate(self, action, risk_score: float):
        domain = action.get("domain", "code")
        threshold = self.thresholds.get(domain, 50)

        if risk_score < threshold * 0.5:
            return "SAFE"
        elif risk_score < threshold:
            return "SANDBOX"
        elif risk_score < threshold + 20:
            return "ESCALATE"
        else:
            return "BLOCK"
