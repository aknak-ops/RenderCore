import csv
import os
from datetime import datetime

def log_history(entry):
    log_path = "logs/history.csv"
    os.makedirs(os.path.dirname(log_path), exist_ok=True)

    is_new = not os.path.exists(log_path)
    with open(log_path, 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ["id", "prompt", "status", "start_time", "end_time", "duration", "output"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if is_new:
            writer.writeheader()
        writer.writerow(entry)
