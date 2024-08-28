from pprint import pprint

suits = ['diamonds', 'spades', 'hearts', 'clubs']
numbers = [('A', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8), ('9', 9), ('10', 10),
           ('J', 11), ('Q', 12), ('k', 13)]

deck_of_cards = []

for number in numbers:
    for suit in suits:
        answer = number + ' of ' + suit
        deck_of_cards.append(answer)

# pprint('this is a deck of cards:')
# pprint(deck_of_cards)

from random import shuffle
def card_shuffler(deck_of_cards:list):
    shuffle(deck_of_cards)
    return deck_of_cards

# shuffle(deck_of_cards)
# pprint(deck_of_cards)
#
# player_1_hand = deck_of_cards.pop()
#
# print(player_1_hand)
#
# print(len(deck_of_cards))
#
