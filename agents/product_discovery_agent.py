from __future__ import annotations
from tool_client import ToolClient
client = ToolClient()

def run(state):
    result = client.search_products("pasta", max_results=5) if "pasta" in state["prompt"].lower() else client.search_products("organic milk", max_results=5)
    state["selected_products"] = list(result["items"])
    state["tool_results"].append({"agent": "product_discovery", "tool": "search_products", "output": {"items": list(result["items"]), "count": result["count"]}})
    return state
