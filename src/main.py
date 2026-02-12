from psychopy import visual, event
import config

# helper functions
def safe_quit(win):
    if win:
        win.close()

def check_for_quit(win):
    if config.QUIT_KEY in event.getKeys():
        safe_quit(win)

# create window
def create_window():
	return visual.Window(
		size = config.WINDOW_SIZE,
		fullscr = config.FULLSCREEN,
		color = config.BACKGROUND_COLOR,
		units = 'height',
	)

# placeholder for future
def show_placeholder(win):
    text = visual.TextStim(
		win,
		text = 'Press Esc to exit.',
		color = config.TEXT_COLOR,
		height = 0.03
	)
    
    while True:
        text.draw()
        win.flip()
        check_for_quit(win)

def main():
    win = create_window()
    
    show_placeholder(win)

if __name__ == '__main__':
    main()