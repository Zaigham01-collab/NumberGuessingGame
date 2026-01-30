import random 

randomnumber = random.randint(1,20)
count = 0
print ("Guessing Number Game")
Gameover = True
while Gameover :
    guess = int(input ("please enter a number between 1,20:"))
    count +=1
    if count == 3:
        Gameover = False
    if randomnumber == guess :
       print ("Congratulation, You Won")
    else:
        print("oops, you lose, hahahaha")