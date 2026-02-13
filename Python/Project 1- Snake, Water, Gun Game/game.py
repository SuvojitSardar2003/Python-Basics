# 1. Snake, Water, Gun Game in Python
# We all have played snake, water, gun game in our childhood. If you haven't played it, then you can play it with your friends. It is a very simple game. In this game, there are three options: snake, water, and gun. The rules of the game are as follows:

# - Snake drinks water, so snake wins.
# - Gun kills snake, so gun wins.
# - Water drowns gun, so water wins.

# In this game, you will play against the computer. The computer will randomly choose one of the three options, and you will have to choose one as well. The winner will be decided based on the rules mentioned above.

'''
Docstring for Python.Project 1- Snake, Water, Gun Game.game
1 for snake
0 for water
-1 for gun
'''
import random

computer = random.choice([1,0,-1])
user = input("Enter your choice (snake, water, gun): ").lower()
youDict = {"snake": 1, "water": 0, "gun": -1}
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
elif((youNum == 1 and computer == 0) or (youNum == 0 and computer == -1) or (youNum == -1 and computer == 1)):
    print("You win!")
else:
    print("Computer wins!")