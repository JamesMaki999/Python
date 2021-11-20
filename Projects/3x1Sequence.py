# 3x + 1 Application
# James Maki
# November 19 2021
# This application takes input from user and calculates the 3x + 1 sequence until 1 is reached

# Imports
import os

# Variable Declaration
TX1_Clear = lambda: os.system('clear')
TX1_Calculation_Even = lambda i : i / 2         # Even Formula: x / 2
TX1_Calculation_Odd = lambda i : (3 * i) + 1    # Odd Formula: 3x + 1
TX1_Counter = 0
TX1_Total_Value = 0
TX1_User_Input = ""

# Function Declarations
def TX1_Start():
    TX1_Clear()
    print("Welcome to the 3x + 1 Application.")
    TX1_User_Input = input("To use the application, type 'p'. To view Rules, type 'r': ")
    if TX1_User_Input == 'p':
        TX1_Runtime()
    elif TX1_User_Input == 'r':
        TX1_Rules()
    else:
        TX1_Start()

def TX1_Calculation():
    global TX1_Counter, TX1_Total_Value # Global Variables
    while TX1_Total_Value != 1:
        if TX1_Total_Value % 2 == 0:    # Checks if Mod (%) Value is Even
            print("{0} / 2 = {1}".format(int(TX1_Total_Value), int(TX1_Calculation_Even(TX1_Total_Value))))
            TX1_Total_Value = TX1_Calculation_Even(TX1_Total_Value)
            TX1_Counter += 1
        elif TX1_Total_Value % 2 == 1:  # Checks if Mod (%) Value is Odd
            print("3 * {0} + 1 = {1}".format(int(TX1_Total_Value), int(TX1_Calculation_Odd(TX1_Total_Value))))
            TX1_Total_Value = TX1_Calculation_Odd(TX1_Total_Value)
            TX1_Counter += 1
    print("1 has been reached in {} steps.".format(TX1_Counter)) 
    print("Thanks for using this application!")

def TX1_Runtime():
    global TX1_Total_Value
    TX1_Clear()
    TX1_User_Input = input("Please input an integer to be used: ")
    if TX1_User_Input.isnumeric():
        TX1_Total_Value = int(TX1_User_Input)
        TX1_Calculation()
    else:
        TX1_Start()

def TX1_Rules():
    TX1_Clear()
    print("3x + 1 Application Rules:")
    print("1. Input an integer.")
    print("2. Odd numbers are Multiplied by 3 and added by 1.")
    print("3. Even numbers are Divided by 2.")
    print("4. Repeat 2 & 3 until integer of 1 is reached.")
    TX1_User_Input = input("Type 'b' to go back or type 'p' to use the application: ")
    if TX1_User_Input == 'b':
        TX1_Start()
    elif TX1_User_Input == 'p':
        TX1_Runtime()
    else:
        TX1_Rules()

# Functions Implementation
TX1_Start()