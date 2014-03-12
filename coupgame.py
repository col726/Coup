# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from random import shuffle

# <codecell>

actions = ['Income','ForeignAid','Coup','Steal','Assassinate','DukeIncome','Draw']
counters = ['BlockForeignAid','BlockAssassinate','BlockSteal']
#cards = ['Duke','Assassin','Contessa','Captain','Ambassador']
def isAction(action):
    if action in actions:
        return True
    return False

# <codecell>

class Card:
    def __init__(self,name):
        if name not in Game.card_actions:
            raise NameError("Card name not valid, could not be created")
        self.name = name
        self.isActive = True
        self.action = Game.card_actions[name]
        self.counter = Game.card_counters[name]

# <codecell>

class Turn:
    def __init__(self,player):
        self.curr_player = player
        self.turn_stack = []

# <codecell>

class Game:
    
    card_actions = {'Duke':'DukeIncome', 'Assassin':'Assassinate', 'Contessa':None, 'Captain':'Steal', 'Ambassador':'Draw'}
    card_counters = {'Duke':'BlockForeignAid', 'Assassin':None, 'Contessa':'BlockAssassinate', 'Captain':'BlockSteal', 'Ambassador':'BlockSteal'}
    
    def __init__(self,numPlayers):
        if numPlayers > 6:
            raise NameError("Maximum of 6 players per game.")
        if numPlayers < 2:
            raise NameError("Minimum of 2 players per game.")
        self.treasury = float("inf")
        self.players = [Player(i) for i in range(1,numPlayers + 1)]
        self.deck = self.createDeck()
        self.deal()
    def createDeck(self):
        deck = []
        for i in range(0,3):
            for name in Game.card_actions.keys():
                deck.append(Card(name))
        random.shuffle(deck)
        return deck
    def deal(self):
        for player in self.players:
            player.card1 = self.deck.pop()
            player.card2 = self.deck.pop()

# <codecell>

class Player:
    def __init__(self, player_num):
        self.player_num = player_num
        self.player_name = raw_input("Enter Player " + str(player_num) + "s name:")

# <codecell>

p = Player(1)

# <codecell>

print p.player_name

# <codecell>

g = Game(5)

# <codecell>

g.players[0].card1.name
print [g.deck[i].name for i in range(0,len(g.deck))]

# <codecell>


