import random
'''
1 for snake 
-1 for water 
0 for gun
'''

computer = random.choice([-1,0,1])
youstr = input("Enter your choise: ")
youDicat = {"s" : 1, "w": -1, "g": 0}
reverseDicat = {1: "snake", -1: "water", 0: "gun"}

you = youDicat[youstr]

print(f"you chose {reverseDicat[you]}\ncomputer chose {reverseDicat[computer]}")

if(computer == you):
    print("Its a draw")

else: 
    if(computer == -1 and you ==1):
        print("you win")
    elif(computer == -1 and you ==0):
        print("you lose")    
    elif(computer == 1 and you == 0):
        print("you win")
    elif(computer == 1 and you == -1):
        print("you lose")
    elif(computer == 0 and you == 1):
        print("you lose")
    elif(computer == 0 and you == -1):
        print("you win")
    else:
       print("somthing went wrong")
  