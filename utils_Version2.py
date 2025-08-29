TAKEN_HANDLES = {"@VyneBot", "@ZyveBot", "@VexScan", "@ZyraHQ", "@MintHQ"}
HISTORY_DB = {
    "@LuxBot": "Sold for $250, last month.",
    "@RareHQ": "Listed for $300, not sold.",
    "@MintCheck": "Sold for $150, 2 weeks ago."
}
def check_availability(handle: str):
    return handle not in TAKEN_HANDLES

def suggest_handles(handle: str):
    base = handle[1:]  # Remove @
    variants = [f"@{base}HQ", f"@{base}Check", f"@{base}Bot", f"@{base}Scan"]
    return [h for h in variants if check_availability(h)]

def get_handle_history(handle: str):
    return HISTORY_DB.get(handle, "No sales history found.")

def check_fraud(handle: str):
    if handle in {"@badbot", "@scamhandle"}:
        return "⚠️ This handle is flagged for fraud risk."
    return "✅ No fraud detected."