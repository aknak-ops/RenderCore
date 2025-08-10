# Locks the camera angle for each type of movement
def get_camera_angle(exercise_type):
    if exercise_type == "2-character":
        return "side view"
    return "3/4 view"
