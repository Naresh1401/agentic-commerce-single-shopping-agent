from __future__ import annotations
from tool_client import ToolClient
client = ToolClient()

def run(state):
    cart = client.create_cart(state["user_id"])
    for product in state.get("selected_products", [])[:5]:
        qty = 2 if product["sku"] == "SKU-PASTA-001" else 1
        cart = client.update_cart(cart["cart_id"], product["sku"], qty)
    state["cart_id"] = cart["cart_id"]
    state["tool_results"].append({"agent": "cart", "tool": "update_cart", "output": cart})
    state["requires_confirmation"] = True
    return state
