"""
Main entry point for the Audio-Visual Attention Experiment.
"""

from psychopy import visual, event, gui, core
import random
import sys

import config
import trials
import utils

def assign_condition_order():
	return random.choice(config.CONDITIONS)

# get participant info
def get_participant_info():
	info = {
		"age": "",
		"gender": ["Male", "Female", "Other"]
	}

	dialog = gui.DlgFromDict(info, title="Participant Info")

	if not dialog.OK:
		return None

	return info


# create window
def create_window():
	return visual.Window(
		size = config.WINDOW_SIZE,
		fullscr = config.FULLSCREEN,
		color = config.BACKGROUND_COLOR,
		units = "height",
	)

def main():

	# Get participant info
	participant_info = get_participant_info()

	if participant_info is None:
		print("Experiment cancelled.")
		return

	order = assign_condition_order()
	print(f"Assigned order: {order}")

	# Create window
	win = create_window()


	try:
		results = trials.run_full_experiment(
			win,
			participant_info,
			order
		)

		print("Experiment completed.")
		print("Results:", results)

	except Exception as e:
		print("Error:", e)

	finally:
		utils.safe_quit(win)

if __name__ == "__main__":
    main()