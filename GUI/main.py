########################################################################################################################
# Name: Chiedozie Ehileme                                                                                              #                                                  
# Date:  June 9th, 2023                                                                                                #
# Description: the goal to develop a runtime software that acts as an ATM machine for a user with the use of OOP.      #
########################################################################################################################

# stores all login info acts as 
accNumbers = {
              "2241323":'2214'   # <--- Number 1
              ,"9388292":'5516'  # <--- Number 2
              ,"2856291":'0291'  # <--- Number 3
              ,"560101":'6373'   # <--- Number 4
              ,"5429910":'4827'  # <--- Number 5
              ,"2851798":'9271'} # <--- Number 6



def mainScreen():
    print()
    print()
    print("######################## Welcome to your account!! ###########################")
    print("Account Number: " +accountNumber)
    print()
    print("Which account are you selecting: ")
    print("1. Checking Account")
    print("2. Savings Account")
    print()
    print("###############################################################################")
    select = input()
    



while True:
    accountNumber = input("Enter your account number: ")
    if accountNumber in accNumbers:
        pin = input("Enter your pin: ")
        if pin in accNumbers[accountNumber]:
            print("************************Succsfully Logged in***************************")
            mainScreen()
            break # exits the loop since login is successful
        else:
            print("########################## INCORRECT PIN #############################")# <----- Prints when incorrect pin number is inputed
            
    else:
        print("########################## INCORRECT ACCOUNT NUMBER #############################")  # <----- Prints when incorrect account number is inputed
        
        
        
        
  

















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