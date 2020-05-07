#! python3
# Second attempt to create a card game. haven't decided what game yet. maybe war?

# Modules
import random, sys#, collections
# (consider switching over to deque from collections module)


'''consider switcing cards to dictionary as well with card value as value sets?'''
# create a deck of cards
def create_deck():
    card = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
    suit = {'Hearts': '♥','Clubs': '♣','Diamonds': '♦','Spades': '♠'}
    root_deck = []
    for x in enumerate(card, 1):
        for y in suit.keys():
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

# retrieve card suit:
def suit(card):
    return card[1]

# flip a card over
def flip():
    player_card = player_deck.pop(0)
    print(len(player_deck))
    computer_card = computer_deck.pop(0)
    print('You played a ' + name(player_card) + ' of ' + suit(player_card))
    print('Your opponenet played a ' + name(computer_card) + ' of ' + suit(computer_card))
    compare(player_card, computer_card)
    
# split deck into two equal decks
def split(new_deck):
    player_deck = new_deck[:(len(new_deck)//2)]
    computer_deck = new_deck[(len(new_deck)//2):]
    return player_deck, computer_deck
        

# compare the two flipped cards and determine who picks up (include WAR option)
def compare(player_card, computer_card):
    play_pile.append(player_card)
    play_pile.append(computer_card)
    if value(player_card) > value(computer_card):
        print('You won the round: opponent picks up.\n')
        for card in play_pile:
            computer_deck.append(card)
    elif value(player_card) < value(computer_card):
        print('You lost the round: you pick up.\n')
        for card in play_pile:
            player_deck.append(card)
    else:
        print("You are tied. It's time for War!")
        war(play_pile) 
        flip()

# war scenario
def war(pile):
    print('Each player places three cards on the pile and then flips to determine a winner.')
    print(player_deck[-3:])
    print(computer_deck[-3:])
    play_pile = play_pile + player_deck[-3:] + computer_deck[-3:]
    print(len(play_pile))
    

            #if cards played are equal value: place three cards each in the pile then flip again to determine a winner.
            #repeat if equal value again. winner gets whole pile (min: 10 cards)
            #if either deck is smaller than 
##    else:
##        print("You're tied. It's time for War!")
##        print('Flip three cards over and then reveal the fourth to determine the winner.')
##        pile = pile + player_deck[-3:] + computer_deck[-3:]
##        print(len(pile))
##        input('press any key to flip the card...')
##        flip()
    print(f'you have {len(player_deck)} cards in your deck, you opponent has {len(computer_deck)} cards left.')
       

# Gameplay:

new_deck = shuffle(create_deck())
player_deck, computer_deck = split(new_deck)
##player_deck = [[(8, 'Eight'), 'Spades'], [(12, 'Queen'), 'Clubs'], [(9, 'Nine'), 'Diamonds'], [(6, 'Six'), 'Hearts'], [(12, 'Queen'), 'Diamonds']]
##computer_deck = [[(8, 'Eight'), 'Spades'], [(11, 'Jack'), 'Clubs'], [(9, 'Nine'), 'Diamonds'], [(6, 'Six'), 'Hearts'], [(13, 'King'), 'Diamonds']]
play_pile = []





# TESTING ZONE!


quit = False

while not quit:
    play = input("Turn a card by pressing any key. ('q' to quit)\n")
    if play.lower() == 'q':
        print('Thank for playing. See you next time!')
        quit = True
        break
    else:
        flip()
    if player_deck == [] or computer_deck == []:
        if computer_deck == []:
            print('\nYou have won the game!')
            break
        else:
            print('\nYour opponent has won the game!')
            break
   

