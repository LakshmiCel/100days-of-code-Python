import time, random
print("""🃏 Welcome to Blackjack!
------------------------
Dealing cards...
""")
# time.sleep(2)
deck = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']*4

player_deck = []
dealer_deck = []
# print(random.choice(deck))
# print(sum(deck))

def dynamic_Ace(list):
    list[list.index(11)] = 1
    print(f'11 changed in {list}')

player_score = []
dealer_score = []
def assign_deck(card, score):
    if card == 'A':
        score.append(11)
    elif card in ('J', 'Q', 'K'):
        score.append(10) 
    else:
        score.append(card)
for i in range(2):
    player_card = random.choice(deck)
    player_deck.append(player_card)
    assign_deck(player_card, player_score)
    deck.remove(player_card)
    dealer_card = random.choice(deck)
    dealer_deck.append(dealer_card)
    assign_deck(dealer_card, dealer_score)
    deck.remove(dealer_card)
    # print( player_card, dealer_card, player_score , dealer_score, 'innerloop')

# if((11 in player_score or 11 in dealer_score) and (sum(player_score) >= 17 or sum(dealer_score) >=17)):
def check_for_replacing_Ace():
    if 11 in player_score and sum(player_score)>= 15:
        dynamic_Ace(player_score)
    if 11 in dealer_score and sum(dealer_score)>= 15:
        dynamic_Ace(dealer_score)

check_for_replacing_Ace()

def display_player_cards():
    print(f"Player cards  -----  {player_deck[-2]}  , {player_deck[-1]} ")

def display_dealer_cards():
    print(f"Dealer cards  -----  X  , {dealer_deck[-1]} ")

# print( player_deck, player_score, dealer_deck, dealer_score)
while sum(player_score) <21 and sum(dealer_score) <21:
    display_player_cards()
    display_dealer_cards()
    player_choice = input("Enter hit or pass to continue or pass away").strip().lower()
    if player_choice == 'hit':
        player_card = random.choice(deck)
        player_deck.append(player_card)
        assign_deck(player_card, player_score)
        deck.remove(player_card)
        display_player_cards()
        # display_dealer_cards()
    if sum(dealer_score) < 17:
        print("Dealer is now choosing the card...")
        dealer_card = random.choice(deck)
        dealer_deck.append(dealer_card)
        assign_deck(dealer_card, dealer_score)
        deck.remove(dealer_card)
        # display_player_cards()
        display_dealer_cards()
    check_for_replacing_Ace()
    if player_choice == 'pass' and sum(dealer_score) >17:
        print("Player passed, Dealer passed...")
        print("Moment of winner declaration...")
        # max_score = max( sum(player_score), sum(dealer_score))
        if sum(player_score) > sum(dealer_score):
            print(f"Player wins with score! {player_score}")
        elif sum(dealer_score) > sum(player_score):
            print(f"Dealer wins! {dealer_score}")
        elif sum(dealer_score) == sum(player_score):
            print(f"Its a tie! {player_score} {dealer_score}")
        exit()

if sum(player_score) > 21:
    print(f"Player busted with {player_score}, Dealer wins.")
elif sum(dealer_score) > 21:
    print(f"Dealer busted with {dealer_score}, Player wins.")
elif sum(player_score) > sum(dealer_score):
    print("Player wins!")
elif sum(dealer_score) > sum(player_score):
    print("Dealer wins!")
else:
    print("It's a tie!")



    
