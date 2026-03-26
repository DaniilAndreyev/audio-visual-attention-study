"""
Config file that stores constants for the Audio-Visual Attention Experiment
"""
from pathlib import Path


REPO_DIR = Path(__file__).resolve().parent.parent

STIMULI_DIR = REPO_DIR / "stimuli"
DATA_DIR = REPO_DIR / "data"

AUDIO_DIR = STIMULI_DIR / "audio"
VIDEO_DIR = STIMULI_DIR / "video"
QUIZ_DIR = STIMULI_DIR / "quiz"


# stimuli files
STORY_BLACK_AUDIO = str(AUDIO_DIR / "black_story.wav")
STORY_VIDEO_AUDIO = str(AUDIO_DIR / "video_story.wav")

VIDEO_FILE = str(VIDEO_DIR / "video.mp4")

QUIZ_BLACK_FILE = str(QUIZ_DIR / "black_quiz.csv")
QUIZ_VIDEO_FILE = str(QUIZ_DIR / "video_quiz.csv")

# data
PARTICIPANT_DATA = str(DATA_DIR / "participant_data.csv")

# screen config
WINDOW_SIZE = (1920, 1080)
FULLSCREEN = True
BACKGROUND_COLOR = "black"
TEXT_COLOR = "white"

FRAME_RATE = 60


# key bindings
QUIT_KEY = "escape"

QUIZ_KEYS = ["1", "2", "3", "4"]

CONTINUE_KEY = "space"

# conditions
BLACK_FIRST = "BLACK_FIRST"
VIDEO_FIRST = "VIDEO_FIRST"

CONDITIONS = [BLACK_FIRST, VIDEO_FIRST]