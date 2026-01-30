import random

randomnumber = random.randint(1,10)
count = 0
print("Guessing Number Game")
Gameover = True
while Gameover:
    guess = int(input("Please Guess a Number Between 1 to 10: "))
    count +=1
    if count == 3:
     Gameover= False
    if randomnumber == guess :
        print("You Won!...")
    else:
        print("You Loss")