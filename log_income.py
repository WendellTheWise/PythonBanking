import os
import time
import random
import datetime
def log_income(income, amount):
    now = datetime.datetime.now()
    with open("incomes.md", "a") as f:
        f.write(f"""\n |{income}| {amount}| {now.strftime("%c")}| \n""")
    return(f"""Income "{income}" Written As Receiving {amount}""")

def last_incomes():
    with open("incomes.md", "r") as f:
        in_logs = f.readlines()
    if len(in_logs) <= 0:
        return "No Income Logged"
    return "".join(in_logs[-10:])

def total_income():
    total = 0
    with open("incomes.md", "r") as f:
        for line in f.readlines():
            if len(line.split("|")) < 3:
                pass
            else:
                total += float(line.split("|")[2])
    return total

def full_income():
    with open("incomes.md", "r") as f:
        full = f.readlines()
    return "".join(full)

def remove_income(item):
    empty = []
    good = False
    found = False
    while good == False:
        good = True
        with open("incomes.md", "r") as f:
            for line in f.readlines():
                if len(line.split("|")) <= 1:
                    found = True
                    pass
                else:
                    if line.split("|")[1] == item:
                        pass
                    else:
                        empty.append(line)
            if found == False:
                print("Sorry, We Could Not Find That Item, Please Try Again")
                input("Press Enter To Continue")
                os.system('clear')
  
    with open("incomes.md", "w") as f:
        for thing in empty:
            f.write(thing)

