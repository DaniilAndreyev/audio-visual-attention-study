"""
Handles experiment flow.
"""

import config
import quiz
import stimuli
import ui


def run_full_experiment(win, _participant_info, order):
    results = {"score_black": None, "score_video": None}

    condition_functions = {
        "black": run_black_condition,
        "video": run_video_condition,
    }

    ordered_conditions = (
        ["black", "video"] if order == config.BLACK_FIRST else ["video", "black"]
    )

    for condition in ordered_conditions:
        score = condition_functions[condition](win)
        results[f"score_{condition}"] = score

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