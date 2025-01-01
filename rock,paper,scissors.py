import random

rpcchoice = ["rock","paper","scissors"]


running=True

while running:
    computer_choice = random.choice(rpcchoice)

    player_choice = input("Choose rock,paper or scissors: ".lower())

    if player_choice == computer_choice:
            print(f"Computer chose {computer_choice}")
            print("Its a tie!")
    elif player_choice == "rock" and computer_choice == "paper":
            print(f"Computer chose {computer_choice}")
            print("Computer wins!")
    elif player_choice == "rock" and computer_choice == "scissors":
            print(f"Computer chose {computer_choice}")
            print("Player wins!")
    elif player_choice == "paper" and computer_choice == "scissors":
            print(f"Computer chose {computer_choice}")
            print("Computer wins!")
    elif player_choice == "paper" and computer_choice == "rock":
            print(f"Computer chose {computer_choice}")
            print("Player wins!")
    elif player_choice == "scissors" and computer_choice == "rock":
        print(f"Computer chose {computer_choice}")
        print("Computer wins!")
    elif player_choice == "scissors" and computer_choice == "paper":
        print(f"Computer chose {computer_choice}")
        print("Player wins!")
    else:
        print("Invalid input. Please try again!")
    playagain = input("Do you want to play again?  (yes/no)")
    if playagain.lower() != "yes":
        print("Thanks for playing")
        running = False

'''useful insight 
instead of using "continue",making the variables/inputs inside the loop works better'''