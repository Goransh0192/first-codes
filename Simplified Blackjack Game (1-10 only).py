import random

playerIn=True
dealerIn=True

print("welcome to blackjack".title())
deck=[1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]
player_hand=[]
dealer_hand=[]
def dealcard(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)

def total(turn):
    total=0
    for card in turn:
        if card in range(0,11):
            total+=card
    return total

def revealDealerhand():
    if len(dealer_hand)==2:
        return dealer_hand[0]
    elif len(dealer_hand)>2:
        return dealer_hand[0],dealer_hand[1]

for _ in range(2):
    dealcard(dealer_hand)
    dealcard(player_hand)

while playerIn or dealerIn:
    print(f"Dealer has {revealDealerhand()} and X")
    print(f"You have {player_hand} for a total of {total(player_hand)}")
    if playerIn:
        stayorhit =  input('1:Stay\n2:Hit\n')
    if total(dealer_hand)>12:
        dealerIn=False
    else:
        dealcard(dealer_hand)
    if stayorhit == '1':
        playerIn=False
    elif stayorhit == '2':
        dealcard(player_hand)
    if total(player_hand)>=18:
        break
    elif total(dealer_hand)>=18:
        break


if total(player_hand) or total(dealer_hand)>=18:
    if total(dealer_hand) == total(player_hand):
        print(f"You have {player_hand} for a {total(player_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}")
        print("You win!")
    elif total(player_hand) == 18:
        print(f"You have {player_hand} for a {total(player_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}")
        print("Blackjack! You win!")
    elif total(dealer_hand) == 18:
        print(f"You have {player_hand} for a total of {total(player_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}")
        print("Blackjack! Dealer wins!")
    elif total(dealer_hand) >= 18:
        print(f"You have {player_hand} for a total of {total(player_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}")
        print("Dealer busted! You win!")
    elif total(player_hand) >= 18:
        print(f"You have {player_hand} for a total of {total(player_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}")
        print("You busted! Dealer wins!")
    elif 18 - total(player_hand) < 18 - total(dealer_hand):
        print(f"You have {player_hand} for a total of {total(player_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}")
        print("You win!")
    elif 18 - total(player_hand) > 18 - total(dealer_hand):
        print(f"You have {player_hand} for a total of {total(player_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}")
        print("Dealer wins!")
    else:
        print(f"You have {player_hand} for a total of {total(player_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}")
        print("Dealer wins!")
#blackjack game simplified 1-10 cards version