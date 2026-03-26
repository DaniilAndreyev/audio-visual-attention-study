'''
Handles Experiment flow
'''
from psychopy import core
import config
import stimuli
import quiz
import ui

def run_full_experiment(win, participant_info, order):

	results = {
		'score_black': None,
		'score_video': None
	}

	if order == config.BLACK_FIRST:
		results['score_black'] = run_black_condition(win)
		results['score_video'] = run_video_condition(win)
	else:
		results['score_video'] = run_video_condition(win)
		results['score_black'] = run_black_condition(win)


	return results

def run_black_condition(win):
	ui.show_listening_instructions(win)
	stimuli.play_audio(win, config.STORY_BLACK_AUDIO)
	ui.show_quiz_instructions(win)
	return quiz.run_quiz(win, config.QUIZ_BLACK_FILE)

def run_video_condition(win):
	ui.show_listening_instructions(win)
	stimuli.play_video_with_audio(win, config.VIDEO_FILE, config.STORY_VIDEO_AUDIO)
	ui.show_quiz_instructions(win)
	return quiz.run_quiz(win, config.QUIZ_VIDEO_FILE)