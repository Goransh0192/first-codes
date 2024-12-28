#number guesser
import random
top_range=int(input("Enter the top range here: "))
number=random.randint(1,top_range)
running=True
while running:
    guess=int(input("ENTER YOUR GUESS"))
    if guess==number:
        print("YOU GUESSED THE NUMBER RIGHT")
        running=False
        break
    elif guess>number:
        print("too high")
    else:
        print("too low")

