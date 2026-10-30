import os
import random
import time
from datetime import datetime

def set_budget(bud_type, budget):
    with open(f"budgets/{bud_type}.md", "w") as f:
        f.write(str(budget))
    with open("budgets/budg_files.md", "r") as f:
        if bud_type.strip() not in f.read().splitlines():
            with open("budgets/budg_files.md", "a") as f:
                f.write(f"{bud_type}\n")
    return f"""Budget Category {bud_type} Set To {budget}"""

def retrieve_budget(budget):
    with open(f"budgets/{budget.strip()}.md", "r") as f:
        budgets = f.read()
    try:
        return float(budgets)
    except:
        return 0

def retrieve_use(budget):
    total = 0
    now = datetime.now()
    now = now.strftime("%Y-%m")
    with open("reset.md", "r") as a:
        a = a.readline()
        with open("expenses.md", "r") as f:
            for count in (f.readlines()):
                count = count.split("|")
                if len(count) <= 1:
                    pass
                elif (count[4]).strip() == budget:
                    if (count[3]).strip()[:7] == now or a.strip()== "false":
                        total += float(count[2])
    return total

def evaluate_budget():
    total = 0

    with open("budgets/budg_files.md".strip(), "r") as f:
        for bu in f:
            if len(bu.strip()) <= 1:
                pass
            else:
                usage = []
                print(f"{bu.strip()}:{retrieve_use(bu.strip())} / {retrieve_budget(bu)}") 
                if float(retrieve_use(bu.strip())) >= float(retrieve_budget(bu)):
                    print("WARNING BUDGET FULLY MAXXED")
                    print("[##########]")
                else:
                    for num in range(1, 11):
                        if (retrieve_use(bu.strip())) >= (retrieve_budget(bu) / 10) * num:
                            usage.append("#")
                        else:
                            usage.append("-")
                    print(f"TOTAL USAGE")
                    print("".join(usage))
            
def remove_budget():
    empty = []
    try:
        with open("budgets/budg_files.md".strip(), "r") as f:
            for lines in f.readlines():
                if len(lines.strip()) <= 0:
                    pass
                elif retrieve_budget(lines) == 0.0:
                    os.remove(f"budgets/{lines.strip()}.md")
                else:
                    empty.append(lines)
        with open("budgets/budg_files.md", "w") as f:
            for thang in empty:
                f.write(thang)
    except:
        pass


def sanitize():
    empty = []
    with open("expenses.md", "r") as f:
        for lines in f.readlines():
            if len(lines.split("|")) < 3:
                empty.append(lines)
            elif (lines.split("|"))[1].strip() == "":
                os.remove(f"budgets/{lines.split("|")[4].strip()}.md")
                pass
            elif lines.split("|")[2].strip() == "":
                os.remove(f"budgets/{lines.split("|")[4].strip()}.md")
                pass
            else:
                try:
                    float(lines.split("|")[2].strip())
                    empty.append(lines)
                except ValueError:
                    os.remove(f"budgets/{lines.split("|")[4].strip()}.md")
                    pass

    with open("expenses.md", "w") as f:
        for thang in empty:
            f.write(thang)
    

    with open("incomes.md", "r") as f:
        empty = []
        for lines in f.readlines():
            if len(lines.split("|")) < 3:
                empty.append(lines)
            elif (lines.split("|"))[1].strip() == "":
                os.remove(f"goals/{lines.split("|")[4].strip()}.md")
                pass
            elif lines.split("|")[2].strip() == "":
                os.remove(f"goals/{lines.split("|")[4].strip()}.md")
                pass
            else:
                try:
                    float(lines.split("|")[2].strip())
                    empty.append(lines)
                except:
                    os.remove(f"goals/{lines.split("|")[4].strip()}.md")
                    pass

    with open("incomes.md", "w") as f:
        for thang in empty:
            f.write(thang)
    