"""
Main entry point for the Audio-Visual Attention Experiment.
"""

from psychopy import visual, gui
import random

import config
import trials
import utils
import ui

def assign_condition_order():
	return random.choice(config.CONDITIONS)

# create window
def create_window():
	return visual.Window(
		size = config.WINDOW_SIZE,
		fullscr = config.FULLSCREEN,
		color = config.BACKGROUND_COLOR,
		units = "height",
		allowStencil=True
	)

def main():
    # Create window
	win = create_window()

	# Get participant info
	participant_info = ui.collect_participant_info(win)

	if participant_info is None:
		print("Experiment cancelled.")
		return

	order = assign_condition_order()
	print(f"Assigned order: {order}")


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