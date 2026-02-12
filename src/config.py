"""
Config file that stores constants for the Audio-Visual Attention Experiment
"""
import os


# directory paths
REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # ../../__file__

STIMULI_DIR = os.path.join(REPO_DIR, "stimuli")
DATA_DIR = os.path.join(REPO_DIR, "data")

AUDIO_DIR = os.path.join(STIMULI_DIR, "audio")
VIDEO_DIR = os.path.join(STIMULI_DIR, "video")
QUIZ_DIR = os.path.join(STIMULI_DIR,)


# stimuli files
STORY_BLACK_AUDIO = os.path.join(AUDIO_DIR, "black_story.wav")
STORY_VIDEO_AUDIO = os.path.join(AUDIO_DIR, "video_story.wav")

VIDEO_FILE = os.path.join(VIDEO_DIR, "video.mp4")

QUIZ_BLACK_FILE = os.path.join(QUIZ_DIR, "black_quiz.csv")
QUIZ_VIDEO_FILE = os.path.join(QUIZ_DIR, "video_quiz.csv")


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