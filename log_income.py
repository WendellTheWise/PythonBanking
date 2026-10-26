import os
import time
import random
import datetime
def log_income(income, amount):
    now = datetime.datetime.now()
    with open("incomes.md", "a") as f:
        f.write(f"""\n |{income}| {amount}| {now.strftime("%c")}\n""")
    with open("income_total.md", "a") as f:
        f.write(str(amount))
        f.write("\n")
    return(f"""Expense "{income}" Written As Costing {amount}""")

def last_incomes():
    with open("incomes.md", "r") as f:
        in_logs = f.readlines()
    return "".join(in_logs[-10:])

def total_income():
    total = 0
    with open("income_total.md", "r") as f:
        for num in f:
            total += int(num)
    return total

