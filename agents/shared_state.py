from __future__ import annotations

from typing import Any, Dict, List, TypedDict


class CommerceState(TypedDict, total=False):
    user_id: str
    cart_id: str
    store_id: str
    prompt: str
    intent: str
    selected_products: List[Dict[str, Any]]
    tool_results: List[Dict[str, Any]]
    requires_confirmation: bool
    final_response: str
