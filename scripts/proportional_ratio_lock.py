# Locks character proportions based on standard anatomy
def enforce_proportions(character_type):
    if character_type == "masculine":
        return "8-head-tall, 3-head shoulder span"
    if character_type == "feminine":
        return "7.5-head-tall, 2.5-head shoulder span"
