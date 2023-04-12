#Create a number guessing game

import random


comguess=random.randint(1,20)
print("For developer's only :",comguess)

for v in range(4,0,-1):
    n=int(input("\nEnter number between 1 to 20 pls "))
    print("Number of chances left :",v)
    

    if comguess==n:
        print("\n GAME OVER !!!")
    elif n>comguess:
        print("Hint : Pls think a lesser number")
    elif n<comguess:
        print("Hint : Please think of higher number")
    else:
        print("\nBetter luck next time sorry ")



