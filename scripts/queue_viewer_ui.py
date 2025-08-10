# Basic CLI/placeholder UI to show queue progress
def show_queue(queue):
    for task in queue:
        print(f"{task['exercise']} - {task['status']}")
