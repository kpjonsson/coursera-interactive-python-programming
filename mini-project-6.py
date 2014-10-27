# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
busted = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.card_list = []

    def __str__(self):
        output = 'Cards on hand: '
        for i in range(len(self.card_list)):
            output += str(self.card_list[i]) + ' '
        return output
    
    def add_card(self, card):
        self.card_list.append(card)

    def get_value(self):
        value = sum(VALUES[card.get_rank()] for card in self.card_list)
        if any(card.get_rank() == 'A' for card in self.card_list):
            if value + 10 <= 21:
                return value + 10
            else:
                return value
        else:
            return value
   
    def draw(self, canvas, pos):
        for i in range(len(self.card_list)):
            card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.card_list[i].rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.card_list[i].suit))
            canvas.draw_image(card_images, card_loc, CARD_SIZE, [(pos[0]+75*i) + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define deck class 
class Deck:
    def __init__(self):
        self.card_list = [Card(suit, rank)
                          for suit in SUITS
                          for rank in RANKS]

    def shuffle(self):
        random.shuffle(self.card_list)

    def deal_card(self):
        card = random.choice(self.card_list)
        return card
        self.card_list.remove(card)
    
    def __str__(self):
        output = 'Cards in deck: '
        for i in range(len(self.card_list)):
            output += str(self.card_list[i]) + ' '
        return output



#define event handlers for buttons
def deal():
    global outcome, in_play, deck, player_hand, dealer_hand, score 
    
    if in_play == True:
        outcome = 'Player gives up.'
        score -= 1
        in_play = False    
    else:
        outcome = 'Hit or stand?'
    
        deck = Deck()
        player_hand = Hand()
        dealer_hand = Hand()
    
        deck.shuffle()
        player_hand.add_card(deck.deal_card())
        player_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())
    
        in_play = True

def hit():
    global deck, player_hand, score, in_play, outcome, busted
 
    if in_play == True:
        player_hand.add_card(deck.deal_card())
    
    if player_hand.get_value() > 21 and in_play == True:
        outcome = "Player's hand is busted"
        score -= 1
        in_play = False
        busted = True
    elif in_play == True:
        outcome = 'Hit or stand?'
       
def stand():
    global deck, player_hand, dealer_hand, score, in_play, outcome, busted
    
    if busted == True:
        outcome = 'Player already lost.'
    else: 
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(deck.deal_card())
    
    if dealer_hand.get_value() > 21 and in_play == True:
        outcome = "Dealer's hand is busted. Player wins!"
        score += 1
        in_play = False
    elif player_hand.get_value() <= dealer_hand.get_value() and in_play == True:
        outcome = 'Dealer wins!'
        score -= 1
        in_play = False
    elif in_play == True:
        outcome = 'Player wins!'
        score += 1
        in_play = False

# draw handler    
def draw(canvas):
    global outcome, in_play
    
    canvas.draw_text("BLACKJACK", [225, 30], 30, 'Black')
    canvas.draw_text("Dealer's hand:", [100, 80], 24, 'Black')
    canvas.draw_text("Player's hand:", [100, 380], 24, 'Black')
    canvas.draw_text(outcome, [100, 550], 24, 'Black')
    canvas.draw_text('Score: ' + str(score), [475, 575], 24, 'Black')
    
    player_hand.draw(canvas, [100, 400])
    dealer_hand.draw(canvas, [100, 100])
    
    if in_play == True:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [100+CARD_BACK_SIZE[0]/2, 100+CARD_BACK_SIZE[1]/2], CARD_BACK_SIZE)
    elif in_play == False:
        canvas.draw_text('New deal?', [100, 590], 24, 'Red')
    
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the grading rubric
