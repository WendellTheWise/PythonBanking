import time
import os
import random
from log_expense import *
from budget import *
from log_income import *
exit = False

while exit == False:
    sanitize()
    remove_budget()
    os.system('clear')
    print(f"""Welcom To Mr Pythons Banking and Management Service

    Total Balance:
    {total_income() - total_expense()}
    
    Your Last 5 Logged Expenses Are
    {last_expense()}
    
    Your Last 5 Logged Incomes Are:
    {last_incomes()}
    
    Your Current Usage Of Your Budgets Are:""")
    {evaluate_budget()}
    print("""

    The Services We Offer Are:
    
    Log Expenses
    Log Income
    See Full Log (Also Lets You Remove Expenses/Income)
    Budget Settings (Set A Budget To 0 To Remove It)
    Exit
    (Please Enter Full Name Of Requested Service, Names In Parenthesis() Should Not Be Typed)
    """)
    request = input("What Service Would You Like To View? ").lower()

    if request == "exit":
        exit = True

    elif request == "log expenses":
        os.system('clear')
        with open("budg_files.md", "r") as f:
            log_expense(input("What Was Your Expenditure For? "), input("How Much Did Your Expenditure Cost? "), input(f"What Budget Category Does This Expediture Belong Too? "))
        print()
        input("Press Enter To Continue")
        os.system('clear')
    elif request == "log income":
        os.system('clear')
        log_income(input("What Was The Reason For Your Income? "), input("You Much Did You Receive? "))
        print()
        input("Press Enter To Continue")
        os.system('clear')
    elif request == "see full log":
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

        input("Press Enter To Contineu")
        os.system('clear')

    elif request == "budget settings":
        os.system('clear')
        set_budget(input("What Will Be The Name Of The Budget Category You Are Changing or Creating? "), input("What Is The New Budget Maximum Amount? "))
        print()
        input("Press Enter To Continue")
        os.system('clear')
