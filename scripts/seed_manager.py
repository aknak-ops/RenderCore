# Assigns and stores seeds for reproducible renders per exercise
def get_seed(exercise_name):
    seeds = {
        "dumbbell_curl": 32819,
        "plank": 34992,
        "kickbox_knee": 99881
    }
    return seeds.get(exercise_name, 11111)
