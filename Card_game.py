# Create a card game called higher or lower.

"""This game requires 2 players and there are 5 rounds. Each player has 5 cards. Each player takes a card from the top of
 their stack and whoever has the highest number gets a point."""
from random import shuffle

# Play
"""Create a for loop that loops over 5 time (5 rounds) and selects which player has the highest card for each round.
The player with the highest card wins a point"""

def card_shuffler(deck_of_cards:list):
    shuffle(deck_of_cards)
    return deck_of_cards


def deck_maker() -> list[tuple[str, int]]:
    suits = ['diamonds', 'spades', 'hearts', 'clubs']
    numbers = [('A', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8), ('9', 9), ('10', 10),
               ('J', 11), ('Q', 12), ('k', 13)]
    new_deck_of_cards = list({})
    for n, v in numbers:
        for s in suits:
            ans = (n + ' of ' + s, v)
            new_deck_of_cards.append(ans)
    return new_deck_of_cards

def higher_or_lower():
    deck_of_cards = deck_maker()
    card_shuffler(deck_of_cards)
    player_1 = {'score': 0, 'hand': []}
    player_2 = {'score': 0, 'hand': []}
    for r in range(5):
        player_1['hand'].append(deck_of_cards.pop())
        player_2['hand'].append(deck_of_cards.pop())
    for i, r in enumerate(player_1['hand']):
        player_1_card_value = player_1['hand'][i][1]
        player_2_card_value = player_2['hand'][i][1]
        if player_1_card_value == player_2_card_value:
            output_results(player_1, player_2, 'It\'s a tie!', i)

        if player_1_card_value > player_2_card_value:
            player_1['score'] += 1
            output_results(player_1, player_2, 'Player 1 wins!', i)

        if player_1_card_value < player_2_card_value:
            player_2['score'] += 1
            output_results(player_1, player_2, 'Player 2 wins!', i)

    player_1_score = player_1['score']
    player_2_score = player_2['score']
    if player_1_score == player_2_score:
        print('It\'s a tie! Nobody won')
    if player_1_score > player_2_score:
        print('Player 1 is the winner of the game!')
    if player_1_score < player_2_score:
        print('Player 2 is the winner of the game!')



def output_results(player_1, player_2, result, index):
    print(f"Player 1's card is {player_1['hand'][index][0]}. Player 2's card is {player_2['hand'][index][0]}.")
    print(result)
    print(f"Player 1 has {player_1['score']} points. Player 2 has {player_2['score']} points.\n")

higher_or_lower()