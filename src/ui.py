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