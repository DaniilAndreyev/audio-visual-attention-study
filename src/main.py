from psychopy import visual, event, gui
import config

# helper functions
def safe_quit(win):
    if win:
        win.close()

def check_for_quit(win):
    if config.QUIT_KEY in event.getKeys():
        safe_quit(win)

# participant info
def get_participant_info():
	while True:
		info = {
			'id': '',
			'age': '',
			'gender': ['Male', 'Female', 'Other']
		}

		dialog = gui.DlgFromDict(info, title='Participant Info')

		if not dialog.OK:
			return None

		if info['id'].strip():
			return info
		gui.Dlg(title='Error', labelButtonOK='OK').addText('Some fields are empty').show()
	

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
    
    # Get participant info
    participant_info = get_participant_info()
    
    if participant_info is None:
        print('Experiment cancelled.')
        return
    
    print(participant_info)
    
    # Create window
    win = create_window()
    
    show_placeholder(win)

if __name__ == '__main__':
    main()