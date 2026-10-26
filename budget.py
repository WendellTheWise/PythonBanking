import os
import random
import time
from log_expense import *
from log_income import *
def set_budget(budget):
    with open("budget.md", "w") as f:
        f.write(str(budget))
    return f"""Budget Set To {budget}"""

def retrieve_budget():
    with open("budget.md", "r") as f:
        budgets = f.read()
    return budgets

def evaluate_budget():
    return (f"{total_income() - total_expense()} / {retrieve_budget()}")

