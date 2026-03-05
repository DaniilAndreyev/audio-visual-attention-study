"""
Handles Stimulus presentation (audio/video)
"""
from psychopy import visual, sound, core, event
import utils

def play_audio(win, audio_file):
    win.color = "black"
    win.flip()

    story = sound.Sound(audio_file)
    story.play()

    clock = core.Clock()

    while clock.getTime() < story.getDuration():
        if "escape" in event.getKeys():
            core.quit()
        core.wait(0.01)

    return True

def play_video_with_audio(win, video_file, audio_file):
	from psychopy import core

	movie = visual.MovieStim(
		win,
		filename=video_file,
		size=(2, 2),
		units='norm'
	)

	story_audio = sound.Sound(audio_file)
	audio_duration = story_audio.getDuration()

	story_audio.play()
	movie.setAutoDraw(True)

	clock = core.Clock()
	clock.reset()

	while clock.getTime() < audio_duration:
		win.flip()
		utils.check_for_quit(win)

	movie.setAutoDraw(False)
	return True