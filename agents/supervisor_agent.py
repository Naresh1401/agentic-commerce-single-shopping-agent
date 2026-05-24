from __future__ import annotations
from mock_llm import classify_intent

def run(state):
    state["intent"] = classify_intent(state["prompt"])
    state.setdefault("tool_results", [])
    return state
