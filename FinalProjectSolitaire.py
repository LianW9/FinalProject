
"""
Lets Play Solitaire!
Lian Welch
Junior
"""
import random

def createDeck():
    existingCards = []
    nums = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    suits = ['Hearts','Diamonds','Clubs','Spades']
    colors = ['Red', 'Black']
    while len(existingCards) < 52:
        num = random.choice(nums)
        suit = random.choice(suits)
        color = random.choice(colors)
        card = color,num,suit
        if card not in existingCards:
            existingCards.append(card)
    return existingCards

def shuffleDeck(existingCards):
    random.shuffle(existingCards)
    
def oneCard(existingCards):
    randomCard= random.choice(existingCards)
    return randomCard

def setUpCards(existingCards):
    table = []
    for _ in range(7):
        card = oneCard(existingCards)
        table.append(card)
        print(_,card)
    wasteCard = "Waste card", card
    print(wasteCard)
    if wasteCard < card and wasteCard[1] == card[1]:
        new = card + (wasteCard)
        print(new)
       
def dealCards():
    deck = createDeck()
    shuffleDeck(deck)
    setUpCards(deck)
    return deck

def playGame():
    deck = dealCards()
    acePile1 = []
    acePile2 = []
    acePile3 = []
    acePile4 = []
    existingCards = []
    nums = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    suits = ['Hearts','Diamonds','Clubs','Spades']
    colors = ['Red', 'Black']
    while len(existingCards) < 52:
        num = random.choice(nums)
        suit = random.choice(suits)
        color = random.choice(colors)
        card = color,num,suit
        if card not in existingCards:
            existingCards.append(card)
    return existingCards
    cardsLeft = 51
    while cardsLeft < 52:
        if card[0] == 'A':
            if card[1] == 'Hearts':
                newPile1 = card + acePile1
                cardsLeft = cardsLeft - 1
            elif card[1] == 'Diamonds':
                newPile2 = card + acePile2
                cardsLeft = cardsLeft - 1
            elif card[1] == 'Clubs':
                newPile3 = card + acePile3
                cardsLeft = cardsLeft - 1
            else:
                newPile4 = card +acePile4
                cardsLeft = cardsLeft - 1
        print("Pile 1", newPile1, "Pile 2", newPile2, "Pile 3", newPile3, "Pile 4",newPile4) 
        if wasteCard < card and wasteCard[1] == card[1]:
            new = card + (wasteCard)
            cardsLeft = cardsLeft - 1
            print(new)
        print(deck)

playGame()
    
