#!/usr/bin/env python3
#Python/Projects/DegreeConverter.py
#James Maki
#July 24, 2021

import os

"""
This program will:
Allow user to input if they want to convert to/from Celsius, Fahrenheit, or Kelvin
Then allow user to input a value to be converted
Allow no duplicate inputs (Cannot convert celsius to itself)
Lastly, Print out the result to the user
"""

User_Con_From, User_Con_To = "", ""
User_Val = 0.0
Val_List = ["c", "f", "k"]

def DC_Convert(c):
    if User_Con_From.lower() == "c" and User_Con_To == "f":
        User_Inp = (c * 1.8) + 32
        return User_Inp
    elif User_Con_From.lower() == "c" and User_Con_To == "k":
        User_Inp = c + 273.15
        return User_Inp
    elif User_Con_From.lower() == "f" and User_Con_To == "c":
        User_Inp = (c - 32) * .5556
        return User_Inp
    elif User_Con_From.lower() == "f" and User_Con_To == "k":
        User_Inp = (c - 32) * 5/9 + 273.15
        return User_Inp
    elif User_Con_From.lower() == "k" and User_Con_To == "c":
        User_Inp = c - 273.15
        return User_Inp
    elif User_Con_From.lower() == "k" and User_Con_To == "f":
        User_Inp = (c - 273.15) * 9/5 + 32
        return User_Inp

def DC_Start():
    os.system('cls')
    global User_Con_From, User_Con_To
    print("Welcome to DegreeConverter.py\nDeveloped by James Maki")
    User_Con_From = input("\nPlease type which temperature scale that you would like to convert FROM:\n'(C)elsius', '(F)ahrenheit', '(K)elvin'\n")
    if User_Con_From.lower() in Val_List:
        User_Con_To = input("\nPlease type which temperature scale that you would like to convert TO:\n'(C)elsius', '(F)ahrenheit', '(K)elvin'\n")
        if User_Con_From.lower() == User_Con_To.lower():
            DC_Start()
        elif User_Con_To.lower() in Val_List:
            User_Val = float(input("\nPlease type the value that you'd like converted:\n"))
            print("{0} from {1} to {2} is: {3}".format(User_Val, User_Con_From, User_Con_To, DC_Convert(User_Val)))
    else:
        DC_Start()
    User_Rsrt = input("\nWould you like to convert another number?\n(Y)es or (N)o?\n")
    if User_Rsrt.lower() == 'y':
        DC_Start()
    elif User_Rsrt.lower() == 'n':
        exit()
    else:
        print("\nWithout a valid response, we shall just end your session.\nThank you very much for using our degree converter, have a nice day!")
    
    
if __name__ == "__main__":
    DC_Start()