'''
Handles Experiment flow
'''
from psychopy import core
import config
import stimuli
import quiz

def run_full_experiment(win, participant_info, order):

	results = {
		'score_black': None,
		'score_video': None
	}

	# ui.show_instructions(win)

	if order == config.BLACK_FIRST:
		results['score_black'] = run_black_condition(win)
		results['score_video'] = run_video_condition(win)
	else:
		results['score_video'] = run_video_condition(win)
		results['score_black'] = run_black_condition(win)


	return results

def run_black_condition(win):
	# stimuli.play_audio(win, config.STORY_BLACK_AUDIO)
	return quiz.run_quiz(win, config.QUIZ_BLACK_FILE)

def run_video_condition(win):
	# stimuli.play_video_with_audio(win, config.VIDEO_FILE, config.STORY_VIDEO_AUDIO)
	return quiz.run_quiz(win, config.QUIZ_VIDEO_FILE)