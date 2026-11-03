"""Система управления заказами."""
from datetime import datetime

orders = []


def add_order(customer, items):
    """Добавляет заказ: customer — имя клиента, items — {товар: количество}."""
    order = {
        "id": len(orders) + 1,
        "customer": customer,
        "items": items,
        "status": "новый",
        "created": datetime.now().isoformat(timespec="seconds"),
    }
    orders.append(order)
    return order
