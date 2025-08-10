import csv
import os

def load_queue(queue_file):
    if not os.path.exists(queue_file):
        return []
    with open(queue_file, newline='', encoding='utf-8') as csvfile:
        return list(csv.DictReader(csvfile))

def save_queue(queue_file, queue):
    fieldnames = ["id", "prompt", "status"]
    with open(queue_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(queue)

def update_status(queue_file, job_id, new_status):
    queue = load_queue(queue_file)
    for job in queue:
        if job["id"] == job_id:
            job["status"] = new_status
    save_queue(queue_file, queue)
