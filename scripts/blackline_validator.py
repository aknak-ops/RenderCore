# Checks if reinforced muscle lines are present
# Triggers re-render if missing
def check_lines(image):
    return "black_lines" in image.metadata
