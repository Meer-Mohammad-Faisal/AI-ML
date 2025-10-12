# 2. The game() function in a program lets a user play a game and returns the score
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
# contains the previous Hi-score. You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score.
import random

def game():
    print("You are playing the game...")
    score = random.randint(1,60)

    #fetch the high score
    with open("chapter9_ps/hiscore.txt") as f:
        hiscore = f.read()#always give me in string
        if(hiscore !=""):
            hiscore = int(hiscore)
        else:
            hiscore = 0


    print(f"your score: {score}")
    if(score>hiscore):
        #write this hiscore to the file
        with open("chapter9_ps/hiscore.txt","w") as f:
            f.write(str(score))