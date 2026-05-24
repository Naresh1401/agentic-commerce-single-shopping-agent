from __future__ import annotations
from tool_client import ToolClient
client = ToolClient()

def run(state):
    priced = []
    for product in state.get("selected_products", []):
        price = client.get_price(product["sku"], state["store_id"])
        priced.append(price)
    state["tool_results"].append({"agent": "pricing", "tool": "get_price", "output": priced})
    return state
