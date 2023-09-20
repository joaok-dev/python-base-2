#!usr/bin/env python3
"""This script is used to create a product registration"""

__version__ = "0.1.0"
__author__ = "joaok"


product = {
    "name": "Pen",
    "colors": ["Blue", "Red"],
    "price": 1.50,
    "dimension": {
        "height": 12.1,
        "width": 0.8,
    },
    "in_stock": True,
    "code": 123456789,
    "codebar": None,
}

customer = {
    "name": "Joao",
}

purchase = {"customer": customer, "product": product["name"], "amount": 3}
purschase_total = product["price"] * purchase["amount"]

print(
    f"The customer {purchase['customer']['name']} bought {purchase['product']} "
    f"in the amount of {purchase['amount']} units "
    f"and the total was {purschase_total}"
)
