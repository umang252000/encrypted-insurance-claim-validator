def cost_anomaly_score(claimed_amount: float, expected_amount: float) -> float:
    """
    Returns anomaly score between 0 and 1
    """
    if expected_amount <= 0:
        return 0.5

    deviation = abs(claimed_amount - expected_amount) / expected_amount

    if deviation < 0.1:
        return 0.0
    elif deviation < 0.3:
        return 0.3
    elif deviation < 0.6:
        return 0.6
    else:
        return 0.9