import sys
from psychopy import core, event

import config


def safe_quit(win):
    if win:
        win.close()
    core.quit()
    sys.exit()

def check_for_quit(win):
    if config.QUIT_KEY in event.getKeys():
        safe_quit(win)