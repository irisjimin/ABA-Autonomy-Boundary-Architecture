class RiskEngine:
    """
    Computes context-aware risk score.
    """

    def compute(self, action: dict) -> float:
        base = 20

        domain = action.get("domain", "code")
        action_type = action.get("type", "")

        # domain risk
        domain_risk = {
            "code": 10,
            "communication": 25,
            "system": 40,
            "finance": 60
        }.get(domain, 20)

        # action risk
        action_risk = {
            "send_email": 20,
            "modify_db": 40,
            "run_script": 30,
            "transfer_money": 70
        }.get(action_type, 10)

        # uncertainty factor
        uncertainty = 10 if action.get("uncertain", False) else 0

        return base + domain_risk + action_risk + uncertainty
