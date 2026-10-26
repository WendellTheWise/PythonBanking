import time
import os
import random
from log_expense import *
from budget import *
from log_income import *
exit = False

while exit == False:
    os.system('clear')
    print(f"""Welcom To Mr Pythons Banking and Management Service
    
    Your Last 5 Logged Expenses Are
    {last_expense()}
    
    Your Last 5 Logged Incomes Are:
    {last_incomes()}
    
    Your Current Usage Of Your Budget Is:
    {evaluate_budget()}
    
    The Services We Offer Are:
    
    Log Expenses
    Log Income
    See Full Log
    Budget Settings
    Exit
    (Please Enter Full Name Of Requested Service)
    """)
    request = input("What Service Would You Like To View").lower()

    if request == "exit":
        exit = True

    elif request == "log expenses":
        pass
    
    elif request == "log income":
        pass
    
    elif request == "see full log":
        pass
    
    elif request == "budget settings":
        pass

