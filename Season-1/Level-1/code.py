'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

from collections import namedtuple
from decimal import *

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

# moral of the story, 1000.00 should be 100_000 integers

def validorder(order: Order):
    debits = Decimal(0)
    credits = Decimal(0)

    for item in order.items:
        if item.type == 'payment':
            credits += Decimal(item.amount)
        elif item.type == 'product':
            debits += Decimal(item.amount) * Decimal(item.quantity)
        else:
            return "Invalid item type: %s" % item.type

    if debits > Decimal(99_999):
        return 'Total amount payable for an order exceeded'

    if int(credits - debits):
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, credits - debits)
    else:
        return "Order ID: %s - Full payment received!" % order.id