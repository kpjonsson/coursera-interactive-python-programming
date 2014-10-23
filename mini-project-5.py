# implementation of card game - Memory

import simplegui
import random

cards = range(0,8) + range(0,8)

# helper function to initialize globals
def new_game():
    global cards, state, index_1, index_2, exposed, counter
    
    state = 0
    counter = 0
    index_1 = 0
    index_2 = 0
    exposed = [False for i in range(len(cards))]
    random.shuffle(cards)
     
# define event handlers
def mouseclick(pos):
    global exposed, state, index_1, index_2, counter
    
    if state == 0:
        index_1 = list(pos)[0]/50
        
        # flip if unflipped
        if exposed[index_1] == False:
            exposed[index_1] = True
            
        state = 1
            
    elif state == 1:
        
        index_2 = list(pos)[0]/50
        
        # flip if unflipped
        if exposed[index_2] == False:
            exposed[index_2] = True
          
        state = 2
        counter += 1
        label.set_text("Turns = " + str(counter))
            
    elif state == 2:
        
        # check if the same number
        if cards[index_1] != cards[index_2]:
            exposed[index_1] = False
            exposed[index_2] = False
            
        index_1 = list(pos)[0]/50  
        
        # flip if unflipped
        if exposed[index_1] == False:
            exposed[index_1] = True
            
        state = 1 
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global cards, exposed
    
    for i in range(len(cards)):
        if exposed[i] == True:
            canvas.draw_text(str(cards[i]), [25+i*50, 62], 30, "White")
        else:
            canvas.draw_line((25+i*50, 0), (25+i*50, 100), 45,"Green")
            
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
