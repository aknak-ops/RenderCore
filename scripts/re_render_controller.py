# Re-triggers image generation for flagged images
# e.g., bad lines, cropping, incorrect theme, etc.
def retry_render(image_id):
    print(f"Retrying render for {image_id}")
