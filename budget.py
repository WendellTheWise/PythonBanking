import os
import random
import time
from log_expense import *
from log_income import *

def set_budget(budget, bud_type):
    with open(f"{bud_type}.md", "w") as f:
        f.write(str(budget))
    with open("budg_files.md", "r") as f:
        if bud_type.strip() not in f.read().splitlines():
            with open("budg_files.md", "a") as f:
                f.write(f"{bud_type}\n")
    return f"""Budget Category {bud_type} Set To {budget}"""

def retrieve_budget(budget):
    with open(f"{budget.strip()}.md", "r") as f:
        budgets = f.read()
    return float(budgets)

def retrieve_use(budget):
    total = 0
    with open("expenses.md", "r") as f:
        for count in (f.readlines()):
            count = count.split("|")
            if len(count) <= 1:
                pass
            elif (count[4]).strip() == budget:
                total += float(count[2])
    return total

def evaluate_budget():
    total = 0
    with open("budg_files.md".strip(), "r") as f:
        for bu in f:
            if len(bu.strip()) <= 1:
                pass
            else:
                print(f"{bu.strip()}:{retrieve_use(bu.strip())} / {retrieve_budget(bu)}") 
