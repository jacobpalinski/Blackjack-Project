import random

suites=['Hearts','Clubs','Spades','Diamonds']
cards=[2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']

class Card:
    
    def __init__(self,card,value):
        self.card=card
        self.value=value
    
    def dict_card(self):
        return {self.card:self.value}

class Deck:
    
    def __init__(self):
        self.all_cards=[]

        for suite in suites:
            for card in cards:
                if card not in ['Jack','Queen','King','Ace']:
                    self.all_cards.append(Card(card,card).dict_card())
                elif card in ['Jack','Queen','King']:
                    self.all_cards.append(Card(card,10).dict_card())
                else:
                    self.all_cards.append(Card(card,[1,11]).dict_card())
    
    def shuffle_deck(self):
        random.shuffle(self.all_cards)

class Player:
    
    def __init__(self):
        self.cards=[]
        self.points=0

class User(Player):
    
    def dealing(self,Deck):
        card1=Deck.all_cards.pop()
        card2=Deck.all_cards.pop()
        
        self.cards.extend([card1,card2])
        
        for cards in self.cards:
            for card in cards:
                if card=='Ace':
                    ace_value=int(input('How many points do you want the Ace to have? '))

                    if ace_value in [1,11]:
                        self.points+=ace_value
                    else:
                        ace_value=int(input('Ace can only have 1 or 11 points: '))
                        self.points+=ace_value
                else:
                    self.points+=cards[card]
    
    def hit(self,Deck):
        new_card=Deck.all_cards.pop()

        self.cards.append(new_card)

        for card in new_card.keys():
            if card=='Ace':
                ace_value=int(input('How many points do you want the Ace to have? '))

                if ace_value in [1,11]:
                    self.points+=ace_value
                else:
                    ace_value=int(input('Ace can only have 1 or 11 points: '))
                    self.points+=ace_value
            else:
                self.points+=new_card[card]

    def hand(self):
        return f'cards: {self.cards} points: {self.points}'

class Dealer(Player):
    
    def dealing(self,Deck):
        card1=Deck.all_cards.pop()
        card2=Deck.all_cards.pop()

        self.cards.extend([card1,card2])

        for key,value in card1.items():
            if value==[1,11]:
                self.points+=11
            else:
                self.points+=card1[key]
    
    def hit(self,Deck):
        new_card=Deck.all_cards.pop()

        self.cards.append(new_card)

        for card in new_card.keys():
            if card=='Ace':
                self.points+=11
            else:
                self.points+=new_card[card]
        
class Bank_roll:
    def __init__(self,total):
        self.total=int(total)
    
    def bet(self,amount):
        if int(amount) > self.total:
            print('You cannot gamble money you dont have!')
            self.amount=int(input('Please enter value less than total and >0: '))

        if int(amount)<=0:
            print('You have to put some money forward')
            self.amount=int(input('Please enter value less than total and >0: '))
        
        else:
            self.amount=int(amount)

print('Welcome to the Blackjack game')
deck=Deck()
dealer=Dealer()
user=User()
money=input('How much money are you bringing to play with today? ')
bank_roll=Bank_roll(money)

def clear_cards(user,dealer):
    user.cards.clear()
    dealer.cards.clear()
    user.points=0
    dealer.points=0

def user_stay(bank_roll,user,dealer,deck):
            
    dealer.hit(deck)

    if dealer.points>user.points and dealer.points<=21:
        print('Dealer has won this game!')
        bank_roll.total=bank_roll.total-bank_roll.amount
        print(f'You have lost ${bank_roll.amount}')
        deck.all_cards.extend([*dealer.cards,*user.cards])
        clear_cards(user,dealer)
        print(f'You have ${bank_roll.total}')
            
    elif dealer.points>21:
        print('You have won this game!')
        bank_roll.total=bank_roll.total+bank_roll.amount
        print(f'You have won ${bank_roll.amount}')
        deck.all_cards.extend([*dealer.cards,*user.cards])
        clear_cards(user,dealer)
        print(f'You have ${bank_roll.total}')
            
    else:
        user_stay(bank_roll,user,dealer,deck)

def user_hit(bank_roll,user,dealer,deck):
    
    user.hit(deck)

    if user.points>21:
        print('Dealer has won this game!')
        bank_roll.total=bank_roll.total-bank_roll.amount
        print(f'You have lost ${bank_roll.amount}')
        deck.all_cards.extend([*dealer.cards,*user.cards])
        clear_cards(user,dealer)
        print(f'You have ${bank_roll.total}')
    
    else:
        print(user.hand())
        choice=input('Hit or Stay? ')
        if choice=='Hit':
            user_hit(bank_roll,user,dealer,deck)
        elif choice=='Stay':
            user_stay(bank_roll,user,dealer,deck)

while bank_roll.total>0:
    
    amount=input('How much are you willing to bet? ')
    bank_roll.bet(amount)

    deck.shuffle_deck()
    user.dealing(deck)
    dealer.dealing(deck)
    print(user.hand())

    decision=input('Hit or Stay? ')
    
    if decision=='Hit':
        
        user_hit(bank_roll,user,dealer,deck)
            
    
    elif decision=='Stay':
        
        user_stay(bank_roll,user,dealer,deck)
    
    if bank_roll.total==0:
        print('Game is over')
        break
        
        





        
















