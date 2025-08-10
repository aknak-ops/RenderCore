# Tracks characters and style usage across batches
def get_character_data(exercise_name):
    characters = {
        "dumbbell_curl": {"type": "masculine", "theme": "Ocean Mist"},
        "triceps_pushdown": {"type": "feminine", "theme": "Mint Drift"}
    }
    return characters.get(exercise_name, {"type": "masculine", "theme": "default"})
