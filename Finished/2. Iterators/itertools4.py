# Example file for Advanced Python by Joe Marini
# Itertools: combinations and permutations

import itertools


# product() produces the cartesian product of input iterables
cards = "A23456789TJQK"
suits = "SCHD"
deck = list(itertools.product(cards, suits))
print(len(deck), "cards")
print(deck)

# Other way
cards = "A23456789TJQK"
suits = "SCHD"
deck = list(itertools.product(suits, cards))
formatted_deck = [suit + card for suit, card in deck]
print(formatted_deck)


# permutations() creates tuples of a given length with no repeated elements
teams = ("A","B","C","D")
result = itertools.permutations(teams, 2)
print("Permutations",list(result))


# combinations() will create combinations of a given length with no repeats
result = itertools.combinations("ABCD", 3)
print("Combinations",list(result))


# combinations_with_replacement() will create combinations of a given length with repeats
result = itertools.combinations_with_replacement("ABCD", 3)
print(list(result))
