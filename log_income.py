import os
import time
import random

def log_income(income, amount):
    with open("incomes.md", "a") as f:
        f.write(f"""\n |{income}| {amount}|\n""")
    return(f"""Expense "{income}" Written As Costing {amount}""")

def last_incomes():
    with open("incomes.md", "r") as f:
        in_logs = f.readlines()
    return "".join(in_logs[-20:])

for num in range (1,50):
    log_income("test", 2)
print(last_incomes())
