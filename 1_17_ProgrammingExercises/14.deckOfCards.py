#! /usr/bin/python

class Card:
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

class Deck:
    def __init__(self,pack='standard52',count=1):
        self.pack = pack 
        self.count = count

    def getPack(self):
        return self.pack

    def getCount(self):
        return count

    def listCards(self):
        i = 1
        for aCard in self.cards:
            print("Card Number: %3s, Rank: %2s, Suit: %-10s" % (i, aCard.getRank(),aCard.getSuit()))
            i += 1

    def makeCards(self):

        if self.pack == 'standard52':
            suites = ('Clubs','Diamonds','Hearts','Spades')
            ranks  = ('2','3','4','5','6','7','8','9','10','J','Q','K','A')

            cardsList = [] #Using a list here because tuples can't be appended.
            # Will convert this to a tuple after it's formed.
            for c in range(1,self.count+1):
                for s in suites:
                    for r in ranks:
                        cardsList.append(Card(r,s))
            self.cards = tuple(cardsList)

def main():
    myDeck = Deck(count=3)
    myDeck.makeCards()
    myDeck.listCards()

main()

