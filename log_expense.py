import os
import time
import random
import datetime

def log_expense(expense, cost):
    now = datetime.datetime.now()
    with open("expenses.md", "a") as f:
        f.write(f"""\n |{expense}| {cost}| {(now.strftime("%c"))}| \n""")

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

