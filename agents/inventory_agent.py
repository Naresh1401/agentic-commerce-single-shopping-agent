from __future__ import annotations
from tool_client import ToolClient
client = ToolClient()

def run(state):
    available = []
    checks = []
    for product in state.get("selected_products", []):
        inventory = client.check_inventory(product["sku"], state["store_id"])
        checks.append(inventory)
        if inventory["quantity_available"] > 0:
            available.append(product)
    state["selected_products"] = available
    state["tool_results"].append({"agent": "inventory", "tool": "check_inventory", "output": checks})
    return state
