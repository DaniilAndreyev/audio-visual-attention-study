from psychopy import visual, event
from psychopy.hardware import keyboard
import config
import utils


def collect_participant_info(win):

    # Age
    age_label = visual.TextStim(
        win,
        text="Age",
        pos=(0, 0.3),
        height=0.05,
        color=config.TEXT_COLOR,
    )

    age_box = visual.TextBox2(
        win,
        text="",
        placeholder="",
        pos=(0, 0.2),
        letterHeight=0.03,
        size=(0.4, 0.08),
        color=config.TEXT_COLOR,
        
        borderColor="white",
        fillColor=None,
        editable=True,
        overflow="hidden",
        clickable=False
    )
    
    # Gender
    gender_label = visual.TextStim(
        win,
        text="Gender",
        pos=(0, 0),
        height=0.05,
        color=config.TEXT_COLOR,
    )
    
    gender_slider = visual.Slider(
        win,
        fillColor="green",
        ticks=[1, 2, 3, 4, 5],
        labels=["Male", "Female", "Non-Binary", "Other", "Prefer not to say"],
        pos=(0, -0.1),
        size=(0.8, 0.06),
        granularity=1,
        style="radio"
    )

    instruction = visual.TextStim(
        win,
        text="Press SPACE to continue.",
        pos=(0, -0.25),
        height=0.035,
        color=config.TEXT_COLOR
    )
    
    kb = keyboard.Keyboard()

    while True:
        
        age_label.draw()
        age_box.draw()
        gender_label.draw()
        gender_slider.draw()
        instruction.draw()
        
        win.flip()

        utils.check_for_quit(win)

        for key in kb.getKeys():
            if key.name == config.CONTINUE_KEY:
                if age_box.text.strip() != "" and gender_slider.getRating() is not None:
                    
                    kb.clearEvents()

                    return {
                        "age": age_box.text.strip(),
                        "gender": gender_slider.getRating()
                    }

def show_consent_form(win):
    instructions = visual.TextStim(
		win,
		text = """
CONSENT TO PARTICIPATE IN A RESEARCH STUDY

You are invited to participate in a research study about attention and memory.

In this study, you will listen to 2 short stories and then answer a few questions about what you remember.

The experiment will take approximately 5-10 minutes to complete.

Your participation is completely voluntary. You may stop the experiment at any time without any penalty.

Your responses will remain anonymous and will only be used for research purposes.

By continuing, you confirm that you understand the information above and agree to participate in this study.

Press SPACE to agree and continue.
Press ESC to exit the experiment.
            """,
		color = config.TEXT_COLOR,
		height = 0.03,
		units = "height"
	)
    
    while True:
        instructions.draw()
        win.flip()

        keys = event.getKeys()
        if config.QUIT_KEY in keys:
            utils.safe_quit(win)
        if config.CONTINUE_KEY in keys:
            return

def show_listening_instructions(win):
    instructions = visual.TextStim(
		win,
		text = """
You will now listen to a short story.

Please listen carefully to the story while it plays.
You will answer 20 questions about it afterward.

Press SPACE to begin.
            """,
		color = config.TEXT_COLOR,
		height = 0.03,
		units = "height"
	)
    
    while True:
        instructions.draw()
        win.flip()

        keys = event.getKeys()
        if config.QUIT_KEY in keys:
            utils.safe_quit(win)
        if config.CONTINUE_KEY in keys:
            return

def show_quiz_instructions(win):
    instructions = visual.TextStim(
		win,
		text = """
You will now complete a short quiz about the story you just heard.

Please answer each question based on your memory of the story.
If you are unsure of an answer, select the option that seems most accurate.

Use the number keys (1-4) to select your answer.

Press SPACE to begin the quiz.
            """,
		color = config.TEXT_COLOR,
		height = 0.03,
		units = "height"
	)
    
    while True:
        instructions.draw()
        win.flip()

        keys = event.getKeys()
        if config.QUIT_KEY in keys:
            utils.safe_quit(win)
        if config.CONTINUE_KEY in keys:
            return