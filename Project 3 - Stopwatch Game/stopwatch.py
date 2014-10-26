# template for "Stopwatch: The Game"
import simplegui

# define global variables
time_passed = 0
num_of_stops = 0
num_of_success = 0
timer_running = False

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global time_passed
    time_passed += 1

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global tenth_second
    minutes = t / 600
    seconds = (t % 600) / 10
    tenth_second = (t % 600) % 10
    if seconds < 10:
        formatted_seconds = "0" + str(seconds)
    else:
        formatted_seconds = str(seconds)
    formatted_time = str(minutes) + ":" + formatted_seconds + "." + str(tenth_second)
    return formatted_time

# define helper function to display stops and win state
def win_state():
    global num_of_stops, num_of_success
    return str(num_of_success) + "/" + str(num_of_stops)

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(time_passed), (60, 110), 35, "White")
    canvas.draw_text(win_state(), (160, 20), 20, "White")

# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    global timer_running
    timer_running = True
    timer.start()

def stop_handler():
    global num_of_stops, tenth_second, num_of_success, timer_running
    if timer_running == True:
        num_of_stops += 1
        if tenth_second == 0:
            num_of_success += 1
    timer_running = False
    timer.stop()

def reset_handler():
    global time_passed, num_of_stops, num_of_success
    timer.stop()
    time_passed = 0
    num_of_stops = 0
    num_of_success = 0

# create timer
timer = simplegui.create_timer(100, timer_handler)

# create frame
frame = simplegui.create_frame('Stopwatch', 200, 200)
frame.set_canvas_background('Black')
frame.set_draw_handler(draw_handler)

# register event handlers
start_button = frame.add_button('Start', start_handler, 100)
stop_button = frame.add_button('Stop', stop_handler, 100)
reset_button = frame.add_button('Reset', reset_handler, 100)

# start frame
frame.start()