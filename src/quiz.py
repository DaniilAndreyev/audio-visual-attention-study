"""
Handles quiz logic (loading, presenting, scoring)
"""

import csv
from psychopy.constants import FINISHED

def run_quiz(win, quiz_file):
    questions = load_quiz(quiz_file)
    score = 0

    for question in questions:
        is_correct = False; # TODO: present_question(win, question)

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

