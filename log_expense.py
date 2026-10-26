import os
import time
import random

def log_expense(expense, cost):
    with open("expenses.md", "a") as f:
        f.write(f"""\n |{expense}| {cost}|\n""")
    return f"""Expense "{expense}" Written As Costing {cost}"""

def last_expense():
    with open("expenses.md", "r") as f:
        last = f.readlines()
    return "".join(last[-20:])

