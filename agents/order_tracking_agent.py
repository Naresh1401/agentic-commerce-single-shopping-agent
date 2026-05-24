from __future__ import annotations
from tool_client import ToolClient
client = ToolClient()

def run(state):
    order = client.track_order("order_123")
    state["tool_results"].append({"agent": "order_tracking", "tool": "track_order", "output": order})
    state["final_response"] = f"Order {order['order_id']} is {order['status']}."
    return state
