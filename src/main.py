"""
Main entry point for the Audio-Visual Attention Experiment.
"""

import os
import random

from psychopy import logging, visual

import config
import quiz
import trials
import utils
import ui

logging.console.setLevel(logging.ERROR)

FINAL_MESSAGE = r"""
  _____ _                 _                           __                               _   _      _             _   _                _______ 
 |_   _| |__   __ _ _ __ | | __  _   _  ___  _   _   / _| ___  _ __   _ __   __ _ _ __| |_(_) ___(_)_ __   __ _| |_(_)_ __   __ _   / /___ / 
   | | | '_ \ / _` | '_ \| |/ / | | | |/ _ \| | | | | |_ / _ \| '__| | '_ \ / _` | '__| __| |/ __| | '_ \ / _` | __| | '_ \ / _` | / /  |_ \ 
   | | | | | | (_| | | | |   <  | |_| | (_) | |_| | |  _| (_) | |    | |_) | (_| | |  | |_| | (__| | |_) | (_| | |_| | | | | (_| | \ \ ___) |
   |_| |_| |_|\__,_|_| |_|_|\_\  \__, |\___/ \__,_| |_|  \___/|_|    | .__/ \__,_|_|   \__|_|\___|_| .__/ \__,_|\__|_|_| |_|\__, |  \_\____/ 
                                 |___/                               |_|                           |_|                      |___/            
"""


def assign_condition_order():
    return random.choice(config.CONDITIONS)


def create_window():
    return visual.Window(
        size=config.WINDOW_SIZE,
        fullscr=config.FULLSCREEN,
        color=config.BACKGROUND_COLOR,
        units="height",
        allowStencil=True,
    )


def main():
    win = create_window()

    try:
        ui.show_consent_form(win)
        participant_info = ui.collect_participant_info(win)

        if participant_info is None:
            print("Experiment cancelled.")
            return

        order = assign_condition_order()
        print(f"Assigned order: {order}")

        results = trials.run_full_experiment(win, participant_info, order)

        print("Experiment completed.")
        print("Results:", results)

        participant_id = quiz.save_participant_data(participant_info, order, results)
        print(f"Participant ID: {participant_id}")

    except Exception as error:
        print("Error:", error)

    finally:
        os.system("cls" if os.name == "nt" else "clear")
        print(FINAL_MESSAGE)
        utils.safe_quit(win)
        
        

if __name__ == "__main__":
    main()