########################################################################################################################
# Name: Chiedozie Ehileme                                                                                              #                                                  
# Date:  June 9th, 2023                                                                                                #
# Description: the goal to develop a runtime software that acts as an ATM machine for a user with the use of OOP.      #
########################################################################################################################

 1# set rules for making a username and password:
class credentials:
    def __init__(self,name,accountNumber,accountPin) -> None:
        self.name = name
        self.accountNumber = accountNumber
        self.accountPin = accountPin
        
        
        def login(self):
            entered_account_number = input("Enter you account number: ")
            entered_account_pin = input("Enter you account pin: ")
            
            if entered_account_number == self.accountNumber and entered_account_pin == self.accountPin:
                print("Login Succssful!!")
            
            else:
                print("Invalid account number or pin.")
        
# create the user accounts:
credential_1 = credentials("Tanya Wilson",2241323,2214)
credential_2 = credentials("John Smith",9388292,5516)
credential_3 = credentials("Laura Johnson",2856291,2617)
credential_4 = credentials("Micheal Davis",560101,6373)
credential_5 = credentials("Emily Anderson",5429910,4827)
credential_6 = credentials("Christoper Thompson",2851798,9271)

        login()

"""def checkingAccount():
    print("######################## Welcome to your Checking Account!! ###########################")
    print("Account Number: " +accountNumber)
    print()
    

def savingsAccount():
    pass

def mainScreen():
    print()
    print()
    print("************************Succsfully Logged in***************************") # <----- Prints when incorrect pin number is inputed
    print("######################## Welcome to your account!! ###########################")
    print("Account Number: " +accountNumber)
    print()
    print("Which account are you selecting: ")
    print("1. Checking Account")
    print("2. Savings Account")
    print()
    print()
    print()
    print("Log Out")
    print("###############################################################################")
    select = input()
    
    if select == "1":
        checkingAccount()
    elif select == "2":
        savingsAccount()
    elif select.casefold() == "Log Out ":
        Login()
"""


### <----- To authenticate user
accountNumber = input("Enter you account number: ")
while True:
    for key,value in accInfo.items():
        if accountNumber in value:
            accountPin = input("Enter your pin: ")
            if accountPin in accInfo[accountNumber]["accountPin"]:
                mainScreen()
                break
            else: 
                print("########################## INCORRECT PIN NUMBER #############################") # <----- Prints when incorrect account number is inputed
                    
        else:
            print("########################## INCORRECT ACCOUNT NUMBER #############################")# <----- Prints when incorrect pin number is inputed
            accountNumber = input("Enter you account number: ")

    
    






    
    

      
    









"""
from tkinter import*

class atmGUI:
    def __init__(self,mainwindow) -> None:
        self.mainwindow = mainwindow
        self.mainwindow.title("Welcome to Cephrius Bank ")
            
    
           
    # create and configure GUI elements
        self.label = Label(self.mainwindow, text = "Hello")  
        self.label.pack()
        

 
 
 
 
 
 
 
 
window = Tk()
img = PhotoImage(file ="GUI\dollar.png")
atm = atmGUI(window)


window.iconphoto(True,img)
window.geometry("1200x800")
window.mainloop()"""