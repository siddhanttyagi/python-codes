import random
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11,
         'Queen':12, 'King':13, 'Ace':14}
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')


class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]
    def __str__(self):
        return self.rank + " of "+ self.suit
# two_of_hearts=Card("hearts","Two")
# two_of_hearts
# print(two_of_hearts)
# print(two_of_hearts.value)

class Deck:
    def __init__(self):
        self.all_cards=[]
        for itr in suits:
            for itr2 in ranks:
                created_obj=Card(itr,itr2)
                self.all_cards.append(created_obj)
    def shuffle(self):
        random.shuffle(self.all_cards)
    def deal_one(self):
        return self.all_cards.pop()
new_deck=Deck()
print(new_deck.all_cards[1])
for itr in new_deck.all_cards:
    print(itr)

class player:
    def __init__(self,name):
        self.name=name
        self.all_cards=[]
    def remove_one(self):
        return self.all_cards.pop(0)
    def add_card(self,new_cards):
        if type(new_cards)== type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'
player_one=player('ONE')
player_two=player('two')

new_deck=Deck()
new_deck.shuffle()
for x in range(26):
    player_one.add_card(new_deck.deal_one())
    player_two.add_card(new_deck.deal_one())

game_on=True
round_num=0
while game_on:
    round_num+=1
    print(f"Round {round_num}")
    if len(player_one.all_cards)==0:
        print('player two wins')
        game_on=False
        break
    if len(player_two.all_cards)==0:
        print('player two wins')
        game_on=False
        break
    player_one_cards=[]
    player_two_cards=[]
    player_one_cards.append(player_one.remove_one())
    player_two_cards.append(player_two.remove_one())
    at_war=True
    while(at_war==True):
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_card(player_one_cards)
            player_one.add_card(player_two_cards)
            at_war=False
        if player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_card(player_one_cards)
            player_two.add_card(player_two_cards)
            at_war=False
        else:
            print('WAR')
            if(len(player_one.all_cards)<5):
                print('player two wins')
                game_on=False
                break
            elif (len(player_one.all_cards) < 5):
                print('player one wins')
                game_on = False
                break
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())

