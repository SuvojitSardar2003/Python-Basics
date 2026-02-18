# 2. The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file 'Hi-score.txt' which is either blank or contains the previous Hi-score.You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score.

import random

def game():
    print("You are playing the game.")
    score = random.randint(1,62)
    print(f"Your score: {score}")

    # fetch the hi score
    with open("Hi-score.txt") as f:
        hi_score = f.read()
        if(hi_score != ""):
            hi_score = int(hi_score)
        else:
            hi_score = 0

    if(score > hi_score):
        # write this hi_score to the file
        with open("Hi-score.txt", "w") as f:
            f.write(str(score)) #write() takes string only

    return score

game()