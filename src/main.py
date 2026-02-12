from psychopy import visual
import config

def create_window():
	return visual.Window(
		size = config.WINDOW_SIZE,
		fullscr = config.FULLSCREEN,
		color = config.BACKGROUND_COLOR,
		units = 'height',
	)

def main():
    win = create_window()
    
    while True:
        win.flip()
    


if __name__ == "__main__":
    main()