# Audio-Visual Attention Study

A PsychoPy-based experiment that measures story comprehension under two conditions:

- **BLACK_FIRST**: audio-only story first, then video+audio story
- **VIDEO_FIRST**: video+audio story first, then audio-only story

For each condition, participants listen/watch a story and complete a 20-question multiple-choice quiz.

## Project layout

```
.
├── data                              # participant output CSV files
├── docs                              # project documentation
│   ├── architecture.md               # system structure and module responsibilities
│   ├── data-dictionary.md            # output field definitions and meanings
│   └── development.md                # setup and development notes
├── README.md                         # overview, setup, and run instructions
├── src                               # experiment application source code
│   ├── config.py                     # constants: paths, keys, window settings, conditions
│   ├── main.py                       # entry point: initialize app and run the experiment
│   ├── quiz.py                       # load quiz CSVs, render questions, score, save data
│   ├── stimuli.py                    # audio/video stimulus playback functions
│   ├── trials.py                     # run condition order and trial flow logic
│   ├── ui.py                         # consent, participant form, and instruction screens
│   └── utils.py                      # shared helpers (quit handling, safety checks)
└── stimuli                           # media and quiz assets used by the experiment
    ├── audio                         # story audio files
    │   ├── black_story.wav           # audio-only story stimulus (black condition)
    │   └── video_story.wav           # audio track paired with video condition
    ├── quiz                          # question banks per condition
    │   ├── black_quiz.csv            # quiz questions for black/audio condition
    │   └── video_quiz.csv            # quiz questions for video condition
    └── video                         # video stimulus files
        └── surf_study.mp4            # primary video used in the video condition
```

## Requirements

- Python 3.10+
- [PsychoPy](https://www.psychopy.org/)

Install dependencies in your preferred environment:

```bash
pip install psychopy
```

## Run the experiment

From the repository root:

```bash
python src/main.py
```

The experiment will:

1. Show consent form
2. Collect age and gender
3. Randomly assign condition order
4. Run both listening/viewing conditions
5. Save scores to `data/participant_data.csv`

Press `escape` at any point to quit.

## Data output

Results are appended to `data/participant_data.csv` with columns:

- `participant_id`
- `date`
- `age`
- `gender`
- `condition_order`
- `score_black`
- `score_video`

## Notes for researchers

- Condition assignment is random per participant.
- Quiz keys are `1`-`4`.
- Fullscreen and display settings are configured in `src/config.py`.

## Documentation index

- `docs/architecture.md`
- `docs/experiment-protocol.md`
- `docs/development.md`
- `docs/data-dictionary.md`
