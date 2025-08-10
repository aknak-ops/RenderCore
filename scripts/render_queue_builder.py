# Builds render queue from list of exercises
def build_queue(exercise_list):
    return [{"exercise": ex, "status": "queued"} for ex in exercise_list]
