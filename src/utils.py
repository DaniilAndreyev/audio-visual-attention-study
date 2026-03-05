from psychopy import event, core
import sys
import csv
import os
from datetime import datetime
import config

def safe_quit(win):
    if win:
        win.close()
    core.quit()
    sys.exit()

def check_for_quit(win):
    if config.QUIT_KEY in event.getKeys():
        safe_quit(win)

def save_participant_data(participant_info, order, results):
    participant_id = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    csv_file = os.path.join(config.DATA_DIR, "participant_data.csv")
    
    file_exists = os.path.isfile(csv_file)
    
    data_row = {
        'participant_id': participant_id,
        'timestamp': datetime.now().strftime("%Y-%m-%d"),
        'age': participant_info.get('age', ''),
        'gender': participant_info.get('gender', ''),
        'condition_order': order,
        'score_black': results.get('score_black', ''),
        'score_video': results.get('score_video', '')
    }
    
    with open(csv_file, 'a', newline='', encoding='utf-8') as f:
        fieldnames = ['participant_id', 'timestamp', 'age', 'gender', 
                     'condition_order', 'score_black', 'score_video']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        
        if not file_exists:
            writer.writeheader()
        
        writer.writerow(data_row)
    
    print(f"Data saved for participant {participant_id}")
    return participant_id