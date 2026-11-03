"""Система управления заказами."""
from datetime import datetime
from itertools import count

orders = []
_order_numbers = count(1)   # номера не повторяются даже после удалений


def add_order(customer, items):
    """Добавляет заказ: customer — имя клиента, items — {товар: количество}."""
    if not customer.strip():
        raise ValueError("Не указан клиент")
    if not items or any(quantity <= 0 for quantity in items.values()):
        raise ValueError("Нужен хотя бы один товар с количеством больше 0")
    order = {
        "id": next(_order_numbers),
        "customer": customer,
        "items": items,
        "status": "новый",
        "created": datetime.now().isoformat(timespec="seconds"),
    }
    orders.append(order)
    return order
