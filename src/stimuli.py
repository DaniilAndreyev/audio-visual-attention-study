"""
Handles Stimulus presentation (audio/video)
"""
from psychopy import visual, sound, core
import utils

def play_audio(win, audio_file):
	win.color = "black"
	win.flip()

	story = sound.Sound(audio_file)

	story.play()

	core.wait(story.getDuration())

	return True

def play_video_with_audio(win, video_file, audio_file):
	movie = visual.MovieStim3(
		win,
		filename=video_file,
		size=(1, 1),
		flipVert=False,
		flipHoriz=False
	)
	
	
	story_audio = sound.Sound(audio_file)

	story_audio.play()

	while movie.status != visual.FINISHED:

		movie.draw()
		win.flip()

		utils.check_for_quit()

	return True