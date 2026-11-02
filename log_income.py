import os
import time
import random
import datetime
import calendar
from goals import *

def log_income(income, amount, goal):
    now = datetime.datetime.now()
    with open("incomes.md", "a") as f:
        f.write(f"""\n |{income}| {amount}| {(now.strftime("%Y-%m-%d %H:%M"))}| {goal} \n""")
    with open("goals/goal_files.md", "r") as f:
        if goal not in f.read().splitlines():
            set_goals(goal, input("It Appears The Goal You Assigned This To Does Not Exist, We Have Created A New Goal  For You. What Is The Success Point Of This Goal? "))
    return f"""Income "{income}" Written As Receiving {amount}"""

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
    found = False
    with open("incomes.md", "r") as f:
        for line in f.readlines():
            if len(line.split("|")) <= 1:
                pass
            else:
                if line.split("|")[1] == item:
                    found = True
                else:
                    empty.append(line)
        if found == False:
            print("Sorry, We Could Not Find That Item, Please Try Again")
            input("Press Enter To Continue")
            os.system('clear')
  
    with open("incomes.md", "w") as f:
        for thing in empty:
            f.write(thing)

def recurring_income(income_name, amount, goal):
    now = datetime.datetime.now()
    now = now.strftime("%Y-%m-%d")
    with open("times.md", "a") as f:
        f.write(f"{income_name}|{amount}|{goal}|{now}|income|{1}\n")
    log_income(income_name, amount, goal)


def do_recurring_income():
    now = datetime.date.today()
    new = []
    with open("times.md") as f:
        for line in f.read().splitlines():      
            line0 = line.strip().split("|")[0]
            line1 = line.strip().split("|")[1]
            line2 = line.strip().split("|")[2]
            start = line.strip().split("|")[3]
            line4 = line.strip().split("|")[4]
            if line4 == "income":
                line5 = line.strip().split("|")[5]
                count = int(line5)
                start = datetime.date.fromisoformat(start)
                should_be = (now.year - start.year) * 12 + (now.month - start.month)
                if now.day < start.day:
                    should_be -= 1
                should_be += 1
                for num in range((should_be - count)):
                    log_income(line0, line1, line2)
                new.append(f"{line0}|{line1}|{line2}|{start}|{line4}|{should_be}")
            else:
                new.append(line)

    with open("times.md", "w") as q:
        if len(new) == 0:
            q.write(f"{"\n".join(new)}")
        else:
            q.write(f"{"\n".join(new)}\n")


#delete if new works.
# last_month = line3.split("-")[1]
 #               this_month = now.split("-")[1]
   #             last_day = line3.split("-")[2]
    #            this_day = now.split("-")[2]
     #           last_year = line3.split("-")[0]
      #          this_year = now.split("-")[0]
       #         if last_month != this_month or last_year != this_year:
        #            if int(this_month) - int(last_month) >= 2 or int(this_year) - int(last_year) > 0:
         #               for num in range(1, ((int(this_year) - int(last_year)) * 12) + (int(this_month) - int(last_month))):
          #                  log_income(line0, line1,line2)
           #         if int(this_day) >= int(last_day):
            #            log_income(line0, line1, line2)
             #       new.append(f"{line0}|{line1}|{line2}|{line3}|{line4}|{int(line5) + 1}")
              #  else:
               #     new.append(line)