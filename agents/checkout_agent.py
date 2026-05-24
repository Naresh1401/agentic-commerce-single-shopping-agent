from __future__ import annotations
from tool_client import ToolClient
client = ToolClient()

def run(state):
    state["tool_results"].append({"agent": "checkout", "tool": "create_checkout_session", "output": {"status": "waiting_for_confirmation"}})
    state["final_response"] = "Cart is prepared. Please confirm before pickup checkout is created."
    state["requires_confirmation"] = True
    return state
