from psychopy import event, core
import sys
import csv
import os
from datetime import datetime
import config

def safe_quit(win):
    if win:
        win.close()
    core.quit()
    sys.exit()

def check_for_quit(win):
    if config.QUIT_KEY in event.getKeys():
        safe_quit(win)