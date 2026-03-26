"""
Handles quiz logic (loading, presenting, scoring)
"""

import csv
import os
from datetime import datetime

from psychopy import core, event, visual

import config


PARTICIPANT_FIELDS = [
    "participant_id",
    "date",
    "age",
    "gender",
    "condition_order",
    "score_black",
    "score_video",
]


def run_quiz(win, quiz_file):
    questions = load_quiz(quiz_file)
    score = 0

    for question in questions:
        is_correct = render_question(win, question)

        if is_correct:
            score += 1

    return score


def load_quiz(quiz_file):
    with open(quiz_file, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def _build_options_text(question):
    return (
        f"1) {question['option1']}\n\n"
        f"2) {question['option2']}\n\n"
        f"3) {question['option3']}\n\n"
        f"4) {question['option4']}"
    )


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
        text=_build_options_text(q),
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


def save_participant_data(participant_info, order, results):
    file_exists = os.path.isfile(config.PARTICIPANT_DATA)

    participant_id = generate_participant_id(config.PARTICIPANT_DATA)

    data_row = {
        "participant_id": participant_id,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "age": participant_info.get("age", ""),
        "gender": participant_info.get("gender", ""),
        "condition_order": order,
        "score_black": results.get("score_black", ""),
        "score_video": results.get("score_video", ""),
    }

    with open(config.PARTICIPANT_DATA, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=PARTICIPANT_FIELDS)

        if not file_exists:
            writer.writeheader()

        writer.writerow(data_row)

    print(f"Data saved for participant {participant_id}")
    return participant_id


def generate_participant_id(file_path):
    if not os.path.exists(file_path):
        return "P001"

    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    next_id = len(rows) + 1
    return f"P{next_id:03d}"