import random as r
num=r.randint(1,100)
guess=int(input("Guess a number between 1 and 100:"))
count=1
while(guess!=num):
    count+=1
    if(guess<num):
        print("The number is greater than",guess)
    else:
        print("The number is less than ",guess)
    guess=int(input("Guess again!:"))
print(f"You guessed correct!!! in total {count} guesses.")
