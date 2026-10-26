import os
import time
import random
import datetime

def log_expense(expense, cost):
    now = datetime.datetime.now()
    with open("expenses.md", "a") as f:
        f.write(f"""\n |{expense}| {cost}| {(now.strftime("%c"))}\n""")
    with open("expense_total.md", "a") as f:
        f.write(str(cost))
        f.write("\n")
    return f"""Expense "{expense}" Written As Costing {cost}"""

def last_expense():
    with open("expenses.md", "r") as f:
        last = f.readlines()
    return "".join(last[-10:])

def total_expense():
    total = 0
    with open("expense_total.md", "r") as f:
        for num in f:
            total += int(num)
    return total


log_expense('est', 5)