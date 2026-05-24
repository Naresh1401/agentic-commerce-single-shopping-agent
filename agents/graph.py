from __future__ import annotations

import json

from cart_agent import run as cart
from checkout_agent import run as checkout
from coupon_agent import run as coupon
from inventory_agent import run as inventory
from pricing_agent import run as price
from product_discovery_agent import run as discover
from recommendation_agent import run as recommend
from supervisor_agent import run as supervise


def run_graph(prompt: str = "I am making pasta dinner under $40. Add available items to my cart and prepare pickup checkout."):
    state = {
        "user_id": "demo_customer_001",
        "store_id": "store_1001",
        "prompt": prompt,
        "selected_products": [],
        "tool_results": [],
        "requires_confirmation": False,
        "final_response": "",
    }
    for step in [supervise, discover, recommend, price, inventory, coupon, cart, checkout]:
        state = step(state)
    return state


if __name__ == "__main__":
    print(json.dumps(run_graph(), indent=2))
