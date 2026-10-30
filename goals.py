import os
import random
import time

def set_goals(goal_type, goal_amount):
    with open(f"goals/{goal_type}.md", "w") as f:
        f.write(str(goal_amount))
    with open("goals/goal_files.md", "r") as f:
        if goal_type.strip() not in f.read().splitlines():
            with open("goals/goal_files.md", "a") as f:
                f.write(f"{goal_type}\n")
    return f"""Goal Category {goal_type} Set To {goal_amount}"""

def retrieve_goals(goal):
    with open(f"goals/{goal.strip()}.md", "r") as f:
        go = f.read()
    try:
        return float(go)
    except:
        return 0

def retrieve_earned(amount):
    total = 0
    with open("incomes.md", "r") as f:
        for count in (f.readlines()):
            count = count.split("|")
            if len(count) <= 1:
                pass
            elif (count[4]).strip() == amount:
                total += float(count[2])
    return total

def evaluate_goals():
    total = 0
    usage = []
    with open("goals/goal_files.md".strip(), "r") as f:
        for bu in f:
            if len(bu.strip()) <= 1:
                pass
            else:
                usage = []
                print(f"{bu.strip()}:{retrieve_earned(bu.strip())} / {retrieve_goals(bu)}") 
                if float(retrieve_earned(bu.strip())) >= float(retrieve_goals(bu)):
                    print("CONGRATULATIONS, GOAL ACHIEVED")
                    print("[##########]")
                else:
                    for num in range(1, 11):
                        if (retrieve_earned(bu.strip())) >= (retrieve_goals(bu) / 10) * num:
                            usage.append("#")
                        else:
                            usage.append("-")
                    print(f"TOTAL EARNED")
                    print("".join(usage))
            
def remove_goal():
    empty = []
    try:
        with open("goals/goal_files.md".strip(), "r") as f:
            for lines in f.readlines():
                if len(lines.strip()) <= 0:
                    pass
                elif retrieve_goals(lines.strip()) == 0.0:
                    os.remove(f"goals/{lines.strip()}.md")
                else:
                    empty.append(lines)
        with open("goals/goal_files.md", "w") as f:
            for thang in empty:
                f.write(thang)
    except:
        pass
