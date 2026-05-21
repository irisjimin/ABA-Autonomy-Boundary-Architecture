class TrustModel:
    """
    Domain-specific trust tracking system.
    """

    def __init__(self):
        self.trust = {
            "code": 50,
            "communication": 50,
            "system": 40,
            "finance": 30
        }

    def get(self, domain):
        return self.trust.get(domain, 50)

    def update(self, domain, outcome: str):
        if outcome == "SAFE":
            self.trust[domain] += 1
        elif outcome == "SANDBOX":
            self.trust[domain] += 0
        elif outcome == "ESCALATE":
            self.trust[domain] -= 2
        elif outcome == "BLOCK":
            self.trust[domain] -= 5

        # clamp
        self.trust[domain] = max(0, min(100, self.trust[domain]))
