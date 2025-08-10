# Builds prompts dynamically based on metadata
def build_prompt(exercise, theme, camera="3/4 view"):
    return f"{exercise} in {camera} using {theme} theme, centered, with white background"
