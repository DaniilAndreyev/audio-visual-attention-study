"""
Handles quiz logic (loading, presenting, scoring)
"""

import csv
from psychopy import visual, event, core
from psychopy.constants import FINISHED
import config

def run_quiz(win, quiz_file):
    questions = load_quiz(quiz_file)
    score = 0

    for question in questions:
        is_correct = render_question(win, question)

        if is_correct:
            score += 1

    return score

def load_quiz(quiz_file):
    questions = []

    with open(quiz_file, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            questions.append(row)

    return questions

def render_question(win, q):
    question_stim = visual.TextStim(
        win,
        text=q["question"],
        color=config.TEXT_COLOR,
        height=0.06,
        pos=(0, 0.35),
        wrapWidth=1.5
    )

    options_stim = visual.TextStim(
        win,
        text=(
            f"1) {q['option1']}\n\n"
            f"2) {q['option2']}\n\n"
            f"3) {q['option3']}\n\n"
            f"4) {q['option4']}"
        ),
        color=config.TEXT_COLOR,
        height=0.05,
        pos=(0, -0.05),
        wrapWidth=1.5
    )

    event.clearEvents()

    while True:
        question_stim.draw()
        options_stim.draw()
        win.flip()

        keys = event.getKeys(keyList=config.QUIZ_KEYS + [config.QUIT_KEY])

        if config.QUIT_KEY in keys:
            core.quit()

        for key in keys:
            if key in config.QUIZ_KEYS:
                return key == q["correct"]