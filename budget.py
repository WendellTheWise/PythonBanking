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
    return float(budgets)

def evaluate_budget():
    usage = []
    budg = retrieve_budget()
    for num in range(1, 11):
        if (total_expense() - total_income()) >= (budg / 10) * num:
            usage.append("#")
        else:
            usage.append("-")

    if total_expense() - total_income() >= float(retrieve_budget()):
        return f"""Warning! You Have Reached Or Surpassed Your Budget
    {total_expense() - total_income()} / {retrieve_budget()}
    USAGE:[##########]"""

    if (float(retrieve_budget()) - total_expense() + total_income()) <= 1:
        return f"""Caution! You Are Within 1 Dollar Of Your Budget

{total_expense() - total_income()} / {retrieve_budget()}"""

    else:
        return  (f"{total_expense() - total_income()} / {retrieve_budget()}, {"".join(usage)}")
