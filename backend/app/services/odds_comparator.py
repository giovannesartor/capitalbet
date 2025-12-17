def compare_odds(odds_data):
    # For each market (1x2, over/under, BTTS), find max odd
    best = {}
    for market in ["1x2", "over_under", "btts"]:
        best[market] = max(odds_data[market], key=lambda x: x["odd"])
    return best
# Prepared for multiple bookmakers