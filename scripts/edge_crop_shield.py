# Ensures AI output does not cut off edges (head, feet, arms)
# Injects canvas padding into render requests
def apply_padding(canvas):
    return canvas.pad(20, color='white')
