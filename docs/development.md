# Development Guide

## Local setup

1. Create/activate a Python environment.
2. Install PsychoPy:

```bash
pip install psychopy
```

3. Run from repo root:

```bash
python src/main.py
```

## Editing common settings

Most researcher-facing changes can be made in `src/config.py`:

- display (`WINDOW_SIZE`, `FULLSCREEN`, colors)
- key bindings (`QUIT_KEY`, `CONTINUE_KEY`, `QUIZ_KEYS`)
- file locations for stimuli and quiz CSVs

## Adding or updating quiz items

Quiz files are CSVs in `stimuli/quiz/`.
Expected columns:

- `question`
- `option1`
- `option2`
- `option3`
- `option4`
- `correct` (must be `1`, `2`, `3`, or `4`)

## Troubleshooting

- If media does not play, verify paths in `src/config.py` and files under `stimuli/`.
- If output is not saved, confirm `data/` is writable.
- If PsychoPy import fails, verify the active environment and package install.
