# Python Program to shuffle Deck of Cards
# Solution: using random module and itertools

import random, itertools

deck = list(itertools.product(range(1, 14),["Spade", "Club", "Hearts", "Diamonds"]))
# print(deck)

random.shuffle(deck)
# print(deck)

for i in range(5):
    print(deck[i][0], "of", deck[i][1])