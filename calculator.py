# This is a Simple Interest Calculator
# Developed by Kingsley Afamefuna Nwodo
#4-08-2019
# Food for Thought: "The Journey of a thounsand mile STARTS with a STEP"
from colorama import Fore, Back, Style 
from colorama import init
import sys
import os


init()
def main():
    # options functions
    option()

def get_user_choice():
    print(Fore.RED+"\n[1] Simple Interest")
    print("[2] Principal")
    print("[3] Rate")
    print("[4] Time")
    print("[Q/q] Quit.")
    print(Style.RESET_ALL)
    return input("What would you like to calculate? ")

def display_title_bar():
    #clear the terminal screen and displays a title bar.
    os.system('cls')
    print(Fore.GREEN + """\t****************************************************
  \t*** - This is Kingsley's  Interest Calculator!!****
  \t*** - Hello Guys You are Welcome on Board!!*********
 \t****************************************************""")
    print(Style.RESET_ALL)

def option():
    choice =""
    display_title_bar()
    while choice != "q":

        choice = get_user_choice()

        display_title_bar()    
        try:
            if choice == "q" or choice== "Q":
                print("You have chosen to quit the application. Bye for now!!")
                sys.exit()
            else:
                if choice =="1":
                    
                    #int_calculate
                    int_calculate()
                elif choice == "2":
                    #princ_calculate
                    princ_calculate()
            
                elif choice == "3":
                    #rate_calculate
                    rate_calculate()
                    

                elif choice == "4":
                    #time_calculate
                    time_calculate()
                else:
                    print("Please try again!!")
                    
            
        except Exception as e:
           # print(e)
            print(Fore.CYAN + "Please, you entered wrong input. Integer data type is needed!!")
        
        


def int_calculate():
    p =  int(input("Enter the Principal Amount>>>>"))
    r = int(input("Enter the Rate percentage>>>>"))
    t = int(input("Enter the time taken>>>>"))
    i = (p*r*t)/(100)
    print(Fore.YELLOW+"This is the interest answer:==> $%g" %i)

    
        

def princ_calculate():
    i = int(input("Enter the Simple Interest Amount>>>>"))
    r = int(input("Enter the Rate percentage>>>>"))
    t = int(input("Enter the time taken>>>>"))
    p = (i*100)/(r*t)
    print(Fore.YELLOW+"This is the principal amount:==> $%g" %p )

def rate_calculate():
    i= int(input("Enter the Simple Interest Amount>>>>"))
    t = int(input("Enter the time taken>>>>"))
    p =  int(input("Enter the Principal Amount>>>>"))
    r = (i*100)/(p*t)
    print(Fore.YELLOW+"This is the the percentage rate:==> %g" %r + "%")

def time_calculate():
    i= int(input("Enter the Simple Interest Amount>>>>"))
    p =  int(input("Enter the Principal Amount>>>>"))
    r = int(input("Enter the Rate percentage>>>>"))
    t = (i*100)/(p*r)
    print(Fore.YELLOW+"This is the Time:==> %g" %t + "Years")





if __name__ == '__main__':

    main() 