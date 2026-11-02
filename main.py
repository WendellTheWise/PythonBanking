import time
import os
import random
from log_expense import *
from budget import *
from log_income import *
from goals import *
exit = False
os.makedirs("budgets", exist_ok=True)
os.makedirs("goals", exist_ok=True)
while exit == False:
    sanitize()
    remove_budget()
    remove_goal()
    do_recurring_expense()
    do_recurring_income()
    os.system('clear')
    print(f"""Welcome To Mr Pythons Banking and Management Service

    Total Balance:
    {total_income() - total_expense()}

    Your Last 10 Logged Expenses Are
    {last_expense()}
    
    Your Last 10 Logged Incomes Are:
    {last_incomes()}
    
    Your Current Usage Of Your Budgets Are:""")
    {evaluate_budget()}
    print("""
    Your Current Goals Are:""")
    {evaluate_goals()}
    print("""
    The Services We Offer Are:
    
    1: Log Expenses
    2: Log Income
    3: See Full Log (Also Lets You Remove Expenses/Income)
    4: Change Budgets (Set A Budget To 0 To Remove It)
    5: Change Goals(Set A Goals Success Amount To 0 To Remove It)
    6: Automatic Budget Reset Toggle
    7: Recurring Expense (Day Of Recursion Is Set To Today, Requires A First Expense To Be Entered When Selected)
    8: Recurring Income (Day of Recursion Is Set To Today, Requires A First Income To be Entered When Selected)
    9: Exit
    (Please Enter Full Name Of Requested Service Or The Associated Number)
    """)
    request = input("What Service Would You Like To View? ").lower()

    if request == "exit" or request == "9":
        exit = True

    elif request == "log expenses" or request == "1":
        os.system('clear')
        with open("budgets/budg_files.md", "r") as f:
            log_expense(input("What Was Your Expenditure For? "), input("How Much Did Your Expenditure Cost? "), input(f"What Budget Category Does This Expenditure Belong Too? "))
        print()
        input("Press Enter To Continue")
        os.system('clear')
    elif request == "log income" or request == "2":
        os.system('clear')
        log_income(input("What Was The Reason For Your Income? "), input("How Much Did You Receive? "), input(f"What Goal Are You Putting This Money Towards? "))
        print()
        input("Press Enter To Continue")
        os.system('clear')
    elif request == "see full log" or request == "3":
        os.system('clear')
        print(f"""Incomes: 
        {full_income()}
        
Expenditures:
{full_expense()}
        """)
        print()
        print()
        good = False
        while good == False:
            good = True
            remove = input("Would You Like To Remove An Income Or Expenditure? Please Answer With Income, Expenditure, or No: ").lower()
            if remove != "income" and remove != "expenditure" and remove != "no":
                good = False
                os.system('clear')
                print("Please Only Answer With Income, Expenditure, or No")
                input("Press Enter To Continue")
                os.system('clear')
                print(f"""Incomes: 
{full_income()}
        
Expenditures:
{full_expense()}""")
            elif remove == "expenditure":
                os.system('clear')
                print(full_expense())
                remove_expense(input("What Expenditure Would You Like To Remove? "))
            elif remove == "income":
                os.system('clear')
                print(full_income())
                remove_income(input("What Income Would You Like To Remove? "))

        input("Press Enter To Continue")
        os.system('clear')

    elif request == "change budgets" or request == "4":
        os.system('clear')
        print(evaluate_budget())
        set_budget(input("What Will Be The Name Of The Budget Category You Are Changing or Creating? "), input("What Is The New Budget Maximum Amount? "))
        print()
        input("Press Enter To Continue")
        os.system('clear')

    elif request == "change goals" or request == "5":
        os.system('clear')
        print(evaluate_goals())
        set_goals(input("What Will Be The Name Of The Goal You Are Changing or Creating? "), input("What Is The New Goal Success Amount? "))
        print()
        input("Press Enter To Continue")
        os.system('clear')
    
    elif request == "automatic budget reset toggle" or request == "6":
        good = False
        while good == False:
            os.system('clear')
            good = True
            y = input("Would You Like To Turn Automatic Budget Reset On or Off? ").lower()
            if y == "on":
                with open("reset.md", "w") as q:
                    q.write("true")
                    change = input("Monthly Budget Resets Are Now On. Press Enter To Continue")
            elif y == "off":
                with open("reset.md", "w") as q:
                    q.write("false")
                with open("reset.md", "w") as q:
                    change = input("Monthly Budget Resets Are Now Off. Press Enter To Continue")
            else:
                input("Please Enter On or Off")
                good = False
        
    elif request == "recurring expense" or request == "7":
        os.system('clear')
        recurring_expense(input("What Is The Name Of The Recurring Expense? "), input("How Much Is The Recurring Expense? "), input("What Budget Will This Recurring Expense Add To? "))
        os.system('clear')

    elif request == "recurring income" or request == "8":
        os.system('clear')
        recurring_income(input("What Is The Name Of The Recurring Income? "), input("How Much Is The Recurring Income? "), input("What Goal Will This Recurring Income Add To? "))
        os.system('clear')
