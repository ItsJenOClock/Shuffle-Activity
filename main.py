import random

CARDS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
SUITS = ["♥", "♦", "♠", "♣︎"]

deck_of_cards = [f"{card}{suit}" for card in CARDS for suit in SUITS]

# Implement a solution for shuffling a deck of cards without using random.shuffle()
# Using randint() is ok
def shuffle_deck(deck_of_cards):
    shuffled_deck = [] # do not uncomment

    # while len(shuffled_deck) < len(deck_of_cards):
    #     card = deck_of_cards[random.randint(0, len(deck_of_cards) - 1)]
    #     if card not in shuffled_deck:
    #         shuffled_deck.append(card)

    deck_copy = deck_of_cards[:]

    # for i in range(len(deck_of_cards)):
    for card in deck_of_cards:
        card_index = random.randint(0, len(deck_copy) - 1)
        shuffled_deck.append(deck_copy[card_index])
        deck_copy.pop(card_index)

    return shuffled_deck

new_deck = shuffle_deck(deck_of_cards)
print(new_deck)
print(len(new_deck))
