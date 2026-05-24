from __future__ import annotations

from supervisor_agent import run as supervise
from product_discovery_agent import run as discover
from pricing_agent import run as price
from inventory_agent import run as inventory
from cart_agent import run as cart
from checkout_agent import run as checkout
from order_tracking_agent import run as track


def run_single_agent(prompt: str, user_id: str = "demo_customer_001", store_id: str = "store_1001"):
    state = {"prompt": prompt, "user_id": user_id, "store_id": store_id, "tool_results": [], "selected_products": []}
    state = supervise(state)
    if state["intent"] == "order_tracking":
        return track(state)
    if state["intent"] == "cart_update":
        state = discover(state)
        state = inventory(state)
        return cart(state)
    state = discover(state)
    state = price(state)
    state = inventory(state)
    state["final_response"] = "I checked product, price, and inventory using tools."
    return state
