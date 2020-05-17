#! python3
# Second attempt to create a card game.
# Game of war. Play against the computer.
# player will be prompted to flip a card by pressing Enter.

# Modules #

import random 

# functions #

# create a deck of cards
def create_deck():
    cards = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
    shapes = [('Hearts', '♥'), ('Clubs', '♣'), ('Diamonds', '♦'), ('Spades', '♠')]
    root_deck = []
    for x in enumerate(cards, 1):
        for y in shapes:
            root_deck.append([x, y])
    return root_deck

# transfer new deck to playing deck and shuffle it
def shuffle(deck):
    random.shuffle(deck)
    return deck

# retriev card value:
def value(card):
    return card[0][0]

# retrieve card name:
def name(card):
    return card[0][1]

# retrieve card suit name:
def suit(card):
    return card[1][0]

# retrieve card suit symbol:
def symbol(card):
    return card[1][1]

# split deck into two equal decks
def split(new_deck):
    player_deck = new_deck[:(len(new_deck)//2)]
    computer_deck = new_deck[(len(new_deck)//2):]
    play_pile = []
    return player_deck, computer_deck, play_pile

# flip a card over
def flip():
    player_card = player_deck.pop(0)
    computer_card = computer_deck.pop(0)
    print('You played a ' + name(player_card) + ' of ' + suit(player_card))
    print_card(card_face(player_card))
    print('Your opponent played a ' + name(computer_card) + ' of ' + suit(computer_card))
    print_card(card_face(computer_card))
    return player_card, computer_card
    
# compare the two played cards to find the winner of the round
def compare(player_card, computer_card):
    if value(player_card) > value(computer_card):
        print('You won the round: you pick up.\n')
        return 'win'
    elif value(player_card) < value(computer_card):
        print('You lost the round: opponent picks up.\n')
        return 'loss'
    else:
        print(f"You are tied. It's time for War!")
        return 'war'
        

# war scenario adds three cards from each deck to the playing pile.
def war(play_pile, limiter):
    print('Each player places three cards on the pile and then flip the fourth to determine a winner.\n') 
    for i in range(limiter):
        play_pile.append(player_deck.pop(0))
        play_pile.append(computer_deck.pop(0))
    return play_pile


# add played cards to winner's deck
def pickup(deck, pile):
    for card in pile:
        deck.append(card)

        
# creates a card face to be printed on screen      
def card_face(card):
    space = ' '
    face = value(card)
    if value(card) > 10 or value(card) == 1:
       face = name(card)[0] 
    if value(card) == 10:
        space = ''
    sym = symbol(card)
    card_face = ["┌─────────┐",
          f"│{face}{space}       │",
          "│         │",
          "│         │",
          f"│    {sym}    │",
          "│         │",
          "│         │",
          f"│       {space}{face}│",
          "└─────────┘"]
    return card_face

# display the card face
def print_card(card):
    print(*card, sep='\n')

    
# Game Zone #

while True:
    new_deck = shuffle(create_deck())
    player_deck, computer_deck, play_pile = split(new_deck)
    while True:
        print(f'you have {len(player_deck)} cards in your deck, you opponent has {len(computer_deck)} cards left.\n')
        play = input("Turn a card by pressing enter. ('q' to quit)\n")

        if play.lower() == 'q':
            break
            
        else:
            player_card, computer_card = flip()
            play_pile.append(player_card)
            play_pile.append(computer_card)
            result = compare(player_card, computer_card)

            if  result == 'loss':
                pickup(computer_deck, play_pile)
                play_pile = []

            elif result == 'win':
                pickup(player_deck, play_pile)
                play_pile = []

            else:
                if len(player_deck) < 3:
                    limiter = len(player_deck)
                    
                elif len(computer_deck) < 3:
                    limiter  = len(computer_deck)
                    
                else:
                    limiter = 3
                    
                play_pile = war(play_pile, limiter)
                player_card, computer_card = flip()
                play_pile.append(player_card)
                play_pile.append(computer_card)            
                result = compare(player_card, computer_card)

                if  result == 'loss':
                    pickup(computer_deck, play_pile)
                    play_pile = []

                elif result == 'win':
                    pickup(player_deck, play_pile)
                    play_pile = []

                else: 
                    if len(player_deck) < 3:
                        limiter = len(player_deck)
                        
                    elif len(computer_deck) < 3:
                        limiter  = len(computer_deck)
                        
                    else:
                        limiter = 3
                        
                    play_pile = war(play_pile, limiter)

            if len(player_deck) == 0 or len(computer_deck) == 0:

                if len(computer_deck) == 0:
                    print('\nYou have won the game!')
                    break
                else:
                    print('\nYour opponent has won the game!')
                    break
    ans = input(f'Do you want to play again? (Y/N) ')
    if ans[0].lower() == 'y':
        continue   
    else:
        break
print(f'Thank for playing. See you next time!')
