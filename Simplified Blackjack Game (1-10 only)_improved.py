#betting system and play again included

import random

playerIn = True
dealerIn = True

print("Welcome to Blackjack".title())
deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 4
player_hand = []
dealer_hand = []

balance = 10000  # Starting balance

def dealcard(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)

def total(turn):
    total = 0
    for card in turn:
        if card in range(0, 11):
            total += card
    return total

def revealDealerhand():
    if len(dealer_hand) == 2:
        return dealer_hand[0]
    elif len(dealer_hand) > 2:
        return dealer_hand[0], dealer_hand[1]

while balance > 0:
    print(f"Current balance: {balance}")
    bet = float(input("Enter your bet: "))
    if bet > balance:
        print("You cannot bet more than your current balance.")
        continue

    balance -= bet

    player_hand.clear()
    dealer_hand.clear()
    deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 4

    for _ in range(2):
        dealcard(dealer_hand)
        dealcard(player_hand)

    playerIn = True
    dealerIn = True

    while playerIn or dealerIn:
        print(f"Dealer has {revealDealerhand()} and X")
        print(f"You have {player_hand} for a total of {total(player_hand)}")
        if playerIn:
            stayorhit = input('1:Stay\n2:Hit\n')
        if total(dealer_hand) > 12:
            dealerIn = False
        else:
            dealcard(dealer_hand)
        if stayorhit == '1':
            playerIn = False
        elif stayorhit == '2':
            dealcard(player_hand)
        if total(player_hand) >= 18:
            break
        elif total(dealer_hand) >= 18:
            break

    if total(player_hand) or total(dealer_hand) >= 18:
        if total(dealer_hand) == total(player_hand):
            print(f"You have {player_hand} for a {total(player_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}")
            print("It's a tie!")
            balance += bet
        elif total(player_hand) == 18:
            print(f"You have {player_hand} for a {total(player_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}")
            print("Blackjack! You win!")
            balance += bet * 2
        elif total(dealer_hand) == 18:
            print(f"You have {player_hand} for a total of {total(player_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}")
            print("Blackjack! Dealer wins!")
        elif total(dealer_hand) >= 18:
            print(f"You have {player_hand} for a total of {total(player_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}")
            print("Dealer busted! You win!")
            balance += bet * 2
        elif total(player_hand) >= 18:
            print(f"You have {player_hand} for a total of {total(player_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}")
            print("You busted! Dealer wins!")
        elif 18 - total(player_hand) < 18 - total(dealer_hand):
            print(f"You have {player_hand} for a total of {total(player_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}")
            print("You win!")
            balance += bet * 2
        elif 18 - total(player_hand) > 18 - total(dealer_hand):
            print(f"You have {player_hand} for a total of {total(player_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}")
            print("Dealer wins!")
        else:
            print(f"You have {player_hand} for a total of {total(player_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}")
            print("Dealer wins!")

    if balance == 0:
        print("You have run out of balance. Game over!")
        break

    playagain = input("Do you want to play again? (y/n): ")
    if playagain.lower() == 'no' or playagain.lower() == 'n':
        print("Thanks for playing!")
        break
    else:
        continue
'''2024-12-23: You can use a `while` loop to keep the game running until the player decides to quit.'''

