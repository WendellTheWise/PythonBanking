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
    with open("expenses.md", "r") as f:
        for count in f.readlines():
            
def evaluate_budget(buget_file):
    total = 0
    with open("budg_files.md".strip(), "r") as f:
        for bu in f:
            if len(bu) <= 1:
                pass
            else:
                print(f"{bu.strip()}:{retrieve_budget(bu)}")
                while open("expenses.md" "r") as f:
                    check = f.readlines()
                    for num in check:
                        if num == ""
set_budget(5, "test")
(evaluate_budget())