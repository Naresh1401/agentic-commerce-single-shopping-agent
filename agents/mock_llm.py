from __future__ import annotations


def classify_intent(prompt: str) -> str:
    lowered = prompt.lower()
    if "track" in lowered:
        return "order_tracking"
    if "checkout" in lowered or "pickup" in lowered:
        return "meal_planning_cart_checkout"
    if "add" in lowered:
        return "cart_update"
    if "coupon" in lowered or "sale" in lowered:
        return "pricing_coupon"
    return "product_discovery"
