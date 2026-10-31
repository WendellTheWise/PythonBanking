import os
import time
import random
import datetime
from budget import set_budget

def log_expense(expense, cost, budget):
    now = datetime.datetime.now()
    with open("expenses.md", "a") as f:
        f.write(f"""\n |{expense}| {cost}| {(now.strftime("%Y-%m-%d %H:%M"))}| {budget} \n""")
    with open("budgets/budg_files.md", "r") as f:
        if budget not in f.read().splitlines():
            set_budget(budget, input("It Appears The Budget You Assigned This To Does Not Exist, We Have Created A New Budget Category For You. What Is The Money Maximum Of This Budget? "))
    return f"""Expense "{expense}" Written As Costing {cost}"""

def last_expense():
    with open("expenses.md", "r") as f:
        last = f.readlines()
    if len(last) <= 0:
        return "No Expenditures Logged"
    return "".join(last[-10:])

def total_expense():
    total = 0
    with open("expenses.md", "r") as f:
        for line in f.readlines():
            if len(line.split("|")) < 3:
                pass
            else:
                total += float(line.split("|")[2])
    return total

def full_expense():
    with open("expenses.md", "r") as f:
        last = f.readlines()
    return "".join(last)

def remove_expense(item):
    empty = []
    with open("expenses.md", "r") as f:
        for line in f.readlines():
            if len(line.split("|")) <= 1:
                pass
            else:
                if line.split("|")[1] == item:
                    pass
                else:
                    empty.append(line)

    with open("expenses.md", "w") as f:
        for thing in empty:
            f.write(thing)

def recurring_expense(expense, cost, budget):
    now = datetime.datetime.now()
    now = now.strftime("%Y-%m-%d")
    with open("times.md", "a") as f:
        f.write(f"{expense}|{cost}|{budget}|{now}|expense\n")
    log_expense(expense, cost, budget)

def do_recurring_expense():
    now = datetime.datetime.now()
    now = now.strftime("%Y-%m-%d")
    new = []
    with open("times.md") as f:
        for line in f.read().splitlines():      
            line0 = line.strip().split("|")[0]
            line1 = line.strip().split("|")[1]
            line2 = line.strip().split("|")[2]
            line3 = line.strip().split("|")[3]
            line4 = line.strip().split("|")[4]
            if line4 == "expense":
                last_month = line3.split("-")[1]
                this_month = now.split("-")[1]
                last_day = line3.split("-")[2]
                this_day = now.split("-")[2]
                last_year = line3.split("-")[0]
                this_year = now.split("-")[0]
                if last_month != this_month or last_year != this_year:
                    if int(this_month) - int(last_month) >= 2 or int(this_year) != int(last_year) > 0:
                        for num in range(1, ((int(this_year) - int(last_year)) * 12) + (int(this_month) - int(last_month))):
                            log_expense(line0, line1,line2)
                    if int(this_day) >= int(last_day):
                        log_expense(line0, line1, line2)
                    new.append(f"{line0}|{line1}|{line2}|{now}|{line4}")
                else:
                    new.append(line)
            else:
                new.append(line)

    with open("times.md", "w") as q:
        q.write(f"{"\n".join(new)}\n")
