#!/usr/bin/env python3
#PyP3-RockPaperScissors.py
#Python Project 3
#James Maki
#March 24, 2021

import os, time, random #Imported Operating System, Time, & Random

player_score, computer_score = 0, 0 #Set all values to 0

def RPS_Home():
    os.system('cls')       #CT (Clears Terminal)
    print("Let's play a game of Rock, Paper, Scissors.")
    RPS_Scores()           #Calls scores function to display the scores
    msg = input("\nType (P) to begin playing!\n")
    if msg.lower() == 'p': #If msg = p then go to game
        RPS_Game()
    else:                  #If not then restart home
        RPS_Home()

def RPS_Game():
    os.system('cls') #CT (Clears Terminal)
    RPS_Play()       #Calls the play function to begin playing
    RPS_Scores()     #Calls the scores function to display the scores of the computer and player
    RPS_PA()         #Calls the play again function to ask the player if they would like to play again

def RPS_Play():
    os.system('cls') #CT (Clears Terminal)
    pl_mv = input("Rock - 1\nPaper - 2\nScissors - 3\nChoose Wisely!\n")
    pl_mv = int(pl_mv) #Converts the input into an int, for comparison purposes
    if pl_mv in (1, 2, 3): #If pl_mv = either 1, 2, 3 then assign
        if pl_mv == 1:
            rps_pl = "Rock"
        elif pl_mv == 2:
            rps_pl = "Paper"
        elif pl_mv == 3:
            rps_pl = "Scissors"
    else:                  #If not then restart play function
        print("Sorry, please type a valid response!")
        time.sleep(1)
        RPS_Play()
    pc_mv = random.randint(1,3) #Assigns PC move to a random #
    if pc_mv == 1:
        rps_pc = "Rock"
    elif pc_mv == 2:
        rps_pc = "Paper"
    elif pc_mv == 3:
        rps_pc = "Scissors"
    os.system('cls') #CT (Clears Terminal)
    print("Rock...")
    time.sleep(1)
    print("Paper...")
    time.sleep(1)
    print("Scissors...")
    time.sleep(0.5)
    print("Shoot!!!...")
    time.sleep(1)
    os.system('cls') #CT (Clears Terminal)
    print("Player: {0}\nComputer: {1}".format(rps_pl, rps_pc))
    time.sleep(1)
    global computer_score, player_score #Allows for the values to be stored outside of the function
    if pl_mv == pc_mv:
        print("Tie Game")
    else:
        if pl_mv == 1:
            if pc_mv == 2:
                pc_wn()
                computer_score += 1
            elif pc_mv == 3:
                pl_wn()
                player_score += 1
        if pl_mv == 2:
            if pc_mv == 1:
                pl_wn()
                player_score += 1
            elif pc_mv == 3:
                pc_wn()
                computer_score += 1
        if pl_mv == 3:
            if pc_mv == 1:
                pc_wn()
                computer_score += 1
            elif pc_mv == 2:
                pl_wn()
                player_score += 1
    time.sleep(2)

def pc_wn():
    print("Haha, the computer won.")

def pl_wn():
    print("Yes!  Humans win again!.")    

def RPS_PA():
    ans = input("Would you like to play again? 'Y' o 'N':\n")
    if ans.lower() in ("y", "yes", "hell yeah", "si", "yuh"): #If ans value is valid then play again
        RPS_Home()
    elif ans.lower() in ("n", "no", "hell no", "n0", "bruh"): #If ans value is valid then end
        print("Aww, ok.  Thanks for playing!")
    else:
        print("Please type a valid response!")                #If ans value is not valid then restart the function
        RPS_PA()

def RPS_Scores():
    print("\nHIGH SCORES")
    print("Player: {0}".format(player_score))
    print("Computer: {0}\n".format(computer_score))
    time.sleep(0.5)

if __name__ == '__main__':                                    #Starts the programs
    RPS_Home()