# mini-project #5 : Card game - Memory
import simplegui
import random

# helper function to initialize globals
def new_game():
    global cards, exposed, opened, clicks, turns
    cards = range(8) * 2
    random.shuffle(cards)
    exposed = [False for i in range(16)]
    opened = []
    clicks = 0
    turns = 0

# define event handlers
def mouseclick(pos):
    global clicks, turns
    if clicks == 0:
        opened.append(pos[0] // 50)
        exposed[pos[0] // 50] = True
        clicks += 1
        turns = 1
    elif clicks == 1:
        if not (pos[0] // 50 in opened):
           opened.append(pos[0] // 50)
           clicks += 1
           exposed[pos[0] // 50] = True
    else:
        if not (pos[0]//50 in opened):
            if cards[opened[-1]] != cards[opened[-2]]:
                exposed[opened[-1]] = False
                exposed[opened[-2]] = False
                opened.pop()
                opened.pop()
            clicks = 1
            turns += 1
            exposed[pos[0]//50] = True
            opened.append(pos[0] // 50)

# cards are logically 50x100 pixels in size
def draw(canvas):
        label.set_text("Turns = "+str(turns))
        card_pos = 0
        for i in range(16):
            if exposed[i]:
                canvas.draw_text(str(cards[i]), [15 + 50 * i, 70], 40, "White")
            else:
                canvas.draw_polygon([(card_pos, 0), (card_pos, 100), (card_pos + 50, 100), (card_pos + 50, 0)], 1, "Red", "Green")
            card_pos += 50

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()