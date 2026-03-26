# Architecture

## Overview

The experiment is split into small modules with each having their own responsibilities:

- `main.py`: entry point, window creation, end-to-end
- `trials.py`: condition ordering and condition execution
- `stimuli.py`: audio and video presentation
- `quiz.py`: quiz loading, rendering, scoring, and data
- `ui.py`: consent, participant intake, and instruction screens
- `utils.py`: shared quit/safety helpers
- `config.py`: paths, constants, and key bindings

## On runtime

1. `main.main()` creates a PsychoPy window.
2. Consent form is shown.
3. Participant metadata is collected.
4. A condition order is selected.
5. `trials.run_full_experiment()` runs both conditions and returns scores.
6. `quiz.save_participant_data()` appends output to CSV.
7. `utils.safe_quit()` closes resources and exits.

## Config

`config.py` has all constants:

- display settings (`WINDOW_SIZE`, `FULLSCREEN`, colors)
- keyboard bindings (`QUIT_KEY`, `CONTINUE_KEY`, `QUIZ_KEYS`)
- canonical paths for stimuli and output data
- condition names and available orderings

This keeps behavioral adjustments out of task logic.