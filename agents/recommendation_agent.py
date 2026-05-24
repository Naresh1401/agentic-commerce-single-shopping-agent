from __future__ import annotations

def run(state):
    recommendations = ["SKU-SAUCE-001", "SKU-SALAD-001", "SKU-BREAD-001", "SKU-CHEESE-001"]
    seen = {product["sku"] for product in state.get("selected_products", [])}
    state["selected_products"].extend([{"sku": sku, "name": sku} for sku in recommendations if sku not in seen])
    state["tool_results"].append({"agent": "recommendation", "output": recommendations})
    return state
