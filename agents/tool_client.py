from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List
from uuid import uuid4

DATA = json.loads((Path(__file__).resolve().parents[1] / "backend/app/seed/sample_data.json").read_text(encoding="utf-8"))
PRODUCTS = {p["sku"]: p for p in DATA["products"]}
INVENTORY = {(i["store_id"], i["sku"]): i for i in DATA["inventory"]}
CARTS: Dict[str, Dict[str, Any]] = {}


class ToolClient:
    def search_products(self, query: str, category: str | None = None, max_results: int = 5) -> Dict[str, Any]:
        q = query.lower()
        items = []
        for product in PRODUCTS.values():
            haystack = " ".join([product["name"], product["category"], product["brand"], " ".join(product["tags"])]).lower()
            if q in haystack and (not category or product["category"] == category):
                items.append({"sku": product["sku"], "name": product["name"], "category": product["category"], "brand": product["brand"]})
        return {"items": items[:max_results], "count": len(items[:max_results])}

    def check_inventory(self, sku: str, store_id: str) -> Dict[str, Any]:
        return dict(INVENTORY[(store_id, sku)])

    def get_price(self, sku: str, store_id: str) -> Dict[str, Any]:
        product = PRODUCTS[sku]
        return {"sku": sku, "store_id": store_id, "base_price": product["base_price"], "sale_price": product["sale_price"], "loyalty_price": product["loyalty_price"]}

    def create_cart(self, user_id: str) -> Dict[str, Any]:
        cart_id = "cart_" + uuid4().hex[:8]
        CARTS[cart_id] = {"cart_id": cart_id, "user_id": user_id, "items": [], "total": 0.0}
        return CARTS[cart_id]

    def update_cart(self, cart_id: str, sku: str, quantity: int) -> Dict[str, Any]:
        cart = CARTS.setdefault(cart_id, {"cart_id": cart_id, "user_id": "demo_customer_001", "items": [], "total": 0.0})
        cart["items"].append({"sku": sku, "quantity": quantity})
        cart["total"] = round(cart["total"] + PRODUCTS[sku]["loyalty_price"] * quantity, 2)
        return cart

    def validate_coupon(self, coupon_code: str) -> Dict[str, Any]:
        return {"coupon_code": coupon_code, "valid": coupon_code.upper() in {"SAVE10", "PASTA5"}}

    def create_checkout_session(self, cart_id: str, store_id: str) -> Dict[str, Any]:
        return {"checkout_session_id": "checkout_demo", "cart_id": cart_id, "store_id": store_id, "status": "requires_confirmation"}

    def track_order(self, order_id: str) -> Dict[str, Any]:
        return next(order for order in DATA["orders"] if order["order_id"] == order_id)
