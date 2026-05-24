from __future__ import annotations
from tool_client import ToolClient
client = ToolClient()

def run(state):
    coupon = client.validate_coupon("SAVE10")
    state["tool_results"].append({"agent": "coupon", "tool": "validate_coupon", "output": coupon})
    return state
