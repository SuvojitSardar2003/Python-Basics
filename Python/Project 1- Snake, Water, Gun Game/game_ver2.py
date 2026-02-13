# 1. Snake, Water, Gun Game in Python
# We all have played snake, water, gun game in our childhood. If you haven't played it, then you can play it with your friends. It is a very simple game. In this game, there are three options: snake, water, and gun. The rules of the game are as follows:

# - Snake drinks water, so snake wins.
# - Gun kills snake, so gun wins.
# - Water drowns gun, so water wins.

# In this game, you will play against the computer. The computer will randomly choose one of the three options, and you will have to choose one as well. The winner will be decided based on the rules mentioned above.

# Let user play multiple rounds
# Keep score
# End game when user types "exit"

'''
Docstring for Python.Project 1- Snake, Water, Gun Game.game
1 for snake
0 for water
-1 for gun
'''
import random

user_score = 0
computer_score = 0

youDict = {"snake": 1, "water": 0, "gun": -1}

print("Welcome to the Snake, Water, Gun Game!")
print("Enter 'exit' to end the game.")

while True:
    user = input("Enter your choice (snake, water, gun): ").lower()

    if user == "exit":
        print("Thanks for playing!")
        print("\nFinal Score:")
        print("You:", user_score)
        print("Computer:", computer_score)
        break

    if user not in youDict:
        print("Invalid input! Try again.\n")
        continue

    computer = random.choice([1,0,-1])
    youNum = youDict[user]

    if(computer == 1):
        print("Computer chose: snake")
    elif(computer == 0):
        print("Computer chose: water")
    else:
        print("Computer chose: gun")

    print("You chose:", user)

    if(youNum == computer):
        print("It's a tie!")
        user_score += 0
        computer_score += 0
    # elif((youNum == 1 and computer == 0) or (youNum == 0 and computer == -1) or (youNum == -1 and computer == 1)):
    elif((youNum - computer) == 1 or (youNum - computer) == -2):
        print("You win!")
        user_score += 1
        computer_score += 0
    else:
        print("Computer wins!")
        user_score += 0
        computer_score += 1
    print("Current Score -> You:", user_score, "| Computer:", computer_score)
    print("-" * 40)