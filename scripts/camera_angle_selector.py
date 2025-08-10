# Assigns camera view based on exercise type
def select_camera_view(exercise_name, is_partnered=False):
    if is_partnered:
        return "side view"
    return "3/4 view"
