########################################################################################################################
# Name: Chiedozie Ehileme                                                                                              #                                                  
# Date:  June 9th, 2023                                                                                                #
# Description: the goal to develop a runtime software that acts as an ATM machine for a user with the use of OOP.      #
########################################################################################################################

# stores all login info acts as 
account1 = { # <----- Account 1 
    "accountName":   "Tanya Wilson",
    "accountNumber":  "2241323",
    "accountPin":     2214
}

account2 = {
    "accountName":   "John Smith",
    "accountNumber": "9388292",
    "accountPin" :    5516
}

account3 = {
    "accountName":    "Laura Johnson",
    "accountNumber":  "2856291",
    "accountPin" :     2617
}

account4 = {
    "accountName":   "Micheal Davis",
    "accountNumber": "560101",
    "accountPin" :    6373
}

account5 = {
    "accountName":   "Emily Anderson",
    "accountNumber": "5429910",
    "accountPin" :    4827
}

account6 = {
    "accountName":   "Christpher Thompson",
    "accountNumber": "2851798",
    "accountPin" :    9271
}

accInfo = {
    "account1": account1,
    "account2": account2,
    "account3": account3,
    "account4": account4,
    "account5": account5,
    "account6": account6

}


def checkingAccount():
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



### <----- To authenticate user
accountNumber = input("Enter you account number: ")
while True:
    
    if accountNumber == accInfo["accountNumber"]:
        accountPin = input("Enter your pin: ")
        if accountPin in accInfo["accountPin"]:
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