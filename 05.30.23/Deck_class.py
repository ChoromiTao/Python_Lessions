class Player:
    def __init__(self, name: str, score: init = 0):
        self.name = name
        self.hand: list[Deck] = []

    def draw(self, card: Deck):
        self.hand.append()

class Deck:
    suit = ['♠', '♥', '♣', '♦']
    rank = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self, size: int = 52):
        self.deck = [s+r for s in Deck.suit for r in Deck.rank]
    
    def __str__(self):
        return self.deck
    
    def shuffle(self):
        random.shuffle(self.deck)
    
    def take(self):
        return self.deck.pop(0)




my_deck = Deck()

print(my_deck)