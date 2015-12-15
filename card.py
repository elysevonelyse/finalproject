from random import shuffle
from sys import argv

class TarotCard:

    SUITS = ['','Swords','Staves','Pentacles','Cups']

    MINOR_NUMBERS = ['Ace','Two','Three','Four','Five','Six',
        'Seven','Eight','Nine','Ten','Page','Knight','Queen','King']

    MAJOR_NUMBERS = ['The Fool','The Magician','The High Priestess',
        'The Empress','The Emperor','The Heirophant','The Lovers',
        'The Chariot','Justice','The Hermit','Wheel of Fortune',
        'Strength','The Hanged Man','Temperance','The Devil',
        'The Tower','The Star','The Moon','The Sun','Judgment','The World']

    def __init__(self, newSuit, newNumber):

        self.suit = newSuit
        self.number = newNumber

    def stringForSuit(self):

        if self.suit > 0:
            return ' of ' + TarotCard.SUITS[self.suit]
        else: return ''

    def stringForNumber(self):

        if self.suit > 0:
            return TarotCard.MINOR_NUMBERS[self.number]
        else: return TarotCard.MAJOR_NUMBERS[self.number]

    def name(self):

        return self.stringForNumber() + self.stringForSuit() 


class TarotDeck:

    def __init__(self):

        self.cards = []
        self.reset()

    def shuffle(self):

        shuffle(self.cards)
        shuffle(self.cards)

    def deal(self, ncards=1):

        for x in range(0, ncards):
            if len(self.cards): print self.cards.pop().name()

    def reset(self):

        for card in self.cards:
            self.cards.pop()

        for number in range(0, len(TarotCard.MAJOR_NUMBERS)):
            self.cards.append(TarotCard(0, number))

        for suit in range(1, len(TarotCard.SUITS)):
            for number in range(0, len(TarotCard.MINOR_NUMBERS)):
                self.cards.append(TarotCard(suit, number))



# -----------------------------------------------------------------------------


if __name__ == '__main__':
    
    # Arg handling
    USAGE = "Usage: python " + argv[0] + " [cards] (default = 1)"

    if len(argv) > 1:
        if argv[1] in ["h","help","-h","--h","-help","--help"]:
            print USAGE
            exit(1)
        else:
            try: ncards = int(argv[1])
            except: 
                print USAGE
                exit(1)
    else:
        ncards = 1

    # main
    deck = TarotDeck()
    deck.shuffle()
    deck.deal(ncards)
