# Higher or Lower Card Game
This game has 5 rounds and requires 2 players who are given 5 cards each. Each player takes a card from the top of their stack of 5 cardsand whoever has the highest number 
gets a point.

## Description:
The logic of this game relies on python, the random module, functions, for loops, conditional statements and various data structures.


A function called "card_shuffler" takes 1 argument ("deck_of_cards") which is a list and shuffles the cards. A new deck of cards is returned in a different order.

The "deck_maker" function creates a deck of cards. The "suits" variable stores a list of suits as a string, and the "numbers" variable stores a list of tuples 
which contain individual tuples that store key value pairs (string, integer).

An empty variable called "new_deck_of_Cards" is created and stores a dictonary in a list.

A for loop is used to ensure each key value in number for each suit is looped over to create a card and is stored in a variable called "ans" which is a list. 
Next, "ans" is appended to "new_deck_of_card" and is returned.

In the "high_or_lower" function, "deck_maker" is called and stored in a variable called "deck_of_Card" and is shuffled by "card_shuffler".
Following this, variables "player_1" and "player_2" are created. These variable store a dictonary with 2 key value dictionary pairs: {'score': 0, 'hand': 0}.
A for loop is used to assign a card to each player 5 times. The 'hand' value is incremented by 1 in another for loop by using the built-in function "enumerate"
which acts like a counter as it creates indices 1 through 4 for the "0" value in {'hand': 0}.

Below this follows, various conditional if statements is used for each round to check if "player_1" and "player_2" tie, or if either "player_1" or "player_2" win the round. 
If a player wins a round, their 'score' is updated as the value is incremented by 1 point and stored in a variable called "player_1_score" or "player_2_score".
Finally, a function called "output_results", which takes 4 arguments (player_1, player_2, results, index), uses an f string for each outcome to inform the user
of the result for each round.

Next follows a block of conditional if statements to check who has won the entire game by check if the players have equal points, or if one has more than the other. 







