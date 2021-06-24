# Game: Rock Paper Scissor
# Developed Date: 24th June 2021
# Version: 1.0.0
# Developer: HMandro

import os
import time
import random

Loop = True

while Loop == True:
    choice1 = int(input("Enter your choice: Rock(1),Paper(2),Scissor(3),Exit(4)\n"))
    choice2 = random.randint(1,3)

    if choice1 == 1 and choice2 == 1:
        os.system('cls')
        print("You chose Rock.\nCom chose Rock.\n")
        print("Tie!")
        time.sleep(3)
        os.system('cls')

    elif choice1 == 1 and choice2 == 2:
        os.system('cls')
        print("You chose Rock.\nCom chose Paper.\n")
        print("You Lose!")
        time.sleep(3)
        os.system('cls')

    elif choice1 == 1 and choice2 == 3:
        os.system('cls')
        print("You chose Rock.\nCom chose Scissor.\n")
        print("You Win!")
        time.sleep(3)
        os.system('cls')

    elif choice1 == 2 and choice2 == 1:
        os.system('cls')
        print("You chose Paper.\nCom chose Rock.\n")
        print("You Win!")
        time.sleep(3)
        os.system('cls')

    elif choice1 == 2 and choice2 == 2:
        os.system('cls')
        print("You chose Paper.\nCom chose Paper.\n")
        print("Tie!")
        time.sleep(3)
        os.system('cls')

    elif choice1 == 2 and choice2 == 3:
        os.system('cls')
        print("You chose Paper.\nCom chose Scissor.\n")
        print("You Lose!")
        time.sleep(3)
        os.system('cls')

    elif choice1 == 3 and choice2 == 1:
        os.system('cls')
        print("You chose Scissor.\nCom chose Rock.\n")
        print("You Lose!")
        time.sleep(3)
        os.system('cls')

    elif choice1 == 3 and choice2 == 2:
        os.system('cls')
        print("You chose Scissor.\nCom chose Paper.\n")
        print("You Win!")
        time.sleep(3)
        os.system('cls')

    elif choice1 == 3 and choice2 == 3:
        os.system('cls')
        print("You chose Scissor.\nCom chose Scissor.\n")
        print("Tie!")
        time.sleep(3)
        os.system('cls')

    elif choice1 == 4:
        Loop = False

    else:
        print("Wrong Input!")