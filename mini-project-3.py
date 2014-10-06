# template for "Stopwatch: The Game"
import simplegui

# define global variables
t = 0
interval = 100
stops = 0
successes = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    """Formats the second counter t to a timer"""

    while t < 10:
        return '0:00.' + str(t)
    else:
        t = str(t)
        minutes = str(int(t[:-1]) / 60)
        seconds = str(int(t[:-1]) % 60)
        tenths = t[-1]
    
        if int(seconds) < 10:
            return minutes + ':0' + seconds + '.' + tenths
        else:
            return minutes + ':' + seconds + '.' + tenths
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    """Start timer"""
    timer.start()
    
def stop():
    """Stop timer"""
    global t, stops, successes
    timer.stop()
    stops += 1
    
    if t >= 0 and (t % 10) == 0:
        successes += 1
    
def reset():
    """Stop timer and reset"""
    global t
    timer.stop()
    t = 0

# define event handler for timer with 0.1 sec interval
def tick():
    """Increment t by 1 tenth of a second"""
    global t
    t += 1 

# define draw handler
def draw(canvas):
    global stops, successes
    canvas.draw_text(format(t), (50, 80), 40, 'White')
    canvas.draw_text(str(successes) + '/' + str(stops), (90, 110), 20, 'Red')

# create frame
frame = simplegui.create_frame('Stopwatch: The Game', 200, 120)

# register event handlers
frame.set_draw_handler(draw)
frame.add_button('Start', start, 100)
frame.add_button('Stop', stop, 100)
frame.add_button('Reset', reset, 100)
timer = simplegui.create_timer(interval, tick)

# start frame
frame.start()

# Please remember to review the grading rubric
