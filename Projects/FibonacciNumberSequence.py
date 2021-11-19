# Fibonacci Number Sequence
# James Maki
# November 18 2021
# This application takes input from user and prints out the FNS with that many sequences.
# Also my first program written in Ubuntu Linux.

# Imports
import os

# Variable Declarations
FNS_Array = [ 0, 1 ]
FNS_Clear = lambda: os.system('clear')  # Clears Console. Use ('cls') for Windows based systems.
FNS_User_Input = 0

# Function Declarations
def FNS_Start():
    FNS_Clear()
    print("Welcome to the Fibonacci Number Sequence Application.")
    FNS_User_Input = str(input("Please input 'y' to begin or 'n' to exit: "))
    if FNS_User_Input.lower() == 'y':
        FNS_Runtime()
    elif FNS_User_Input.lower() == 'n':
        exit()
    else:
        FNS_Start()

def FNS_For_Loop():
    for i in range(int(FNS_User_Input)):
        print(FNS_Array[i])
        FNS_Array.append(FNS_Array[i] + FNS_Array[i + 1])

def FNS_Input():
    global FNS_User_Input
    FNS_User_Input = input("Please input the amount of sequences, as an integer, to be performed: ")

def FNS_Runtime():
    global FNS_User_Input
    FNS_Clear()
    FNS_Input()
    if FNS_User_Input.isnumeric():
        if int(FNS_User_Input) < 0:
            print("Input cannot be less than 0!")
            FNS_Input()
        elif int(FNS_User_Input) > 0:
            FNS_For_Loop()
            FNS_User_Input = input("Would you like to try again, 'y' or 'n'? ")
            if FNS_User_Input.lower() == 'y':
                FNS_Start()
            else:
                print("Thanks for using this application!")
                exit()
    else:
        FNS_Clear()
        print("Invalid input, please try again.")
        FNS_Start()

# Function Implementation
FNS_Start()