#Create a number guessing game

import random


comguess=random.randint(1,20)
#print("For developer's only :",comguess)

for v in range(5,0,-1):
    n=int(input("\nEnter number between 1 to 20 pls "))
    print("Number of chances left :",v-1)
    

    if comguess==n:
        print("\n You won the game !!!")
    elif n>comguess:
        print("Hint : Pls think a lesser number")
    elif n<comguess:
        print("Hint : Please think of higher number")
    else:
        print("\nBetter luck next time sorry ")

    if comguess==n:
        print("You won the game !!!!!")



