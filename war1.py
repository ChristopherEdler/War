import random

def create_deck(suits = 4, numbers = 13):
     deck = []
     for x in range(suits):
         for y in range(1, numbers+1):
             deck.append(y)

     random.shuffle(deck)
     return deck
#print(create_deck()) Checks to see deck is created

def play_war(deck):
    p1_cards = deck[ : len(deck)/2]
    p2_cards = deck[len(deck)/2 : ]
    #print (p2_cards)
    #return p1_cards

    p1_card = p1_cards[-1]
    p1_cards.pop()
    p2_card = p2_cards[-1]
    p2_cards.pop()
    p1_pile = []
    p2_pile = []

    if p1_card > p2_card:
        p1_cards = p1_cards + [p1_card, p2_card]


    elif p2_card > p1_card:
        p2_cards = p2_cards + [p1_card, p2_card]

    elif p1_card == p2_card:
        p1_pile = p1_cards[-4, ]
        p2_pile = p1_cards[-4,]

        if p1_pile[-1:] > p2_pile[-1:]:
            p1_cards = p1_cards + p2_pile + p1_card + p2_card

        elif p2_pile[-1:] > p1_pile[-1:]:
            p2_cards = p1_cards + p2_pile + p1_card + p2_card

print(play_war([1,1,1,3,3,3]))


