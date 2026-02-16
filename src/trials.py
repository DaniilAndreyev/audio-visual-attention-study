'''
Handles Experiment flow
'''

import config
import stimuli
import ui
from psychopy import core

def run_full_experiment(win, participant_info, order):

	results = {
		'score_black': None,
		'score_video': None
	}

	ui.show_instructions(win)

	if order == config.BLACK_FIRST:
		run_black_condition(win)
		run_video_condition(win)

	else:
		run_video_condition(win)
		run_black_condition(win)
	
	return results

def run_black_condition(win):
	return stimuli.play_audio(win, config.STORY_BLACK_AUDIO)

def run_video_condition(win):
	return stimuli.play_video_with_autdio(
		win,
		config.VIDEO_FILE,
		config.STORY_VIDEO_AUDIO
	)