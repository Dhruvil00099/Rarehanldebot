import random

def calculate_worth(handle: str):
    length = max(0, 20 - len(handle) + 1)
    rarity = random.randint(15, 25)
    brandability = random.randint(8, 15)
    niche = random.randint(5, 10)
    market = random.randint(7, 15)
    dict_penalty = -10 if handle[1:].lower() in DICTIONARY else 0
    fraud_penalty = -5 if handle in FRAUD_LIST else 0
    score = (length * 0.2) + (rarity * 0.25) + (brandability * 0.15) + (niche * 0.10) + \
            (market * 0.15) + (dict_penalty * -0.1) + (fraud_penalty * -0.05)
    breakdown = {
        "Length": length,
        "Rarity": rarity,
        "Brandability": brandability,
        "Niche": niche,
        "Market": market,
        "Dictionary Penalty": dict_penalty,
        "Fraud Penalty": fraud_penalty
    }
    return round(score, 2), breakdown

def analyze_handle(handle: str):
    score, breakdown = calculate_worth(handle)
    lines = [
        f"**Analysis for {handle}:**",
        f"Worth Score: {score}/75",
        "Breakdown:",
    ] + [f"• {k}: {v}" for k, v in breakdown.items()]
    return "\n".join(lines)

DICTIONARY = {"hello", "world", "luxury", "crypto", "mint"}
FRAUD_LIST = {"@badbot", "@scamhandle"}