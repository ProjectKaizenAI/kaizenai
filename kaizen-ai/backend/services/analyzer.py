def analyze_portfolio(tokens):
    top = max(tokens, key=lambda t: t[“value_usd”], default={})
    return {“top_token”: top.get(“symbol”, “N/A”)}