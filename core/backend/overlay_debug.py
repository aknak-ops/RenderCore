from PIL import Image, ImageDraw, ImageFont
import os

def generate_debug_overlay(job_id, plugin_name, status, duration, prompt, output_dir):
    width, height = 640, 400
    bg_color = (30, 30, 30)  # dark gray
    text_color = (255, 255, 255)

    img = Image.new("RGB", (width, height), bg_color)
    draw = ImageDraw.Draw(img)

    lines = [
        f"Job ID: {job_id}",
        f"Plugin: {plugin_name}",
        f"Status: {status}",
        f"Duration: {duration}",
        f"Prompt: {prompt}"
    ]

    try:
        font = ImageFont.truetype("arial.ttf", 16)
    except:
        font = ImageFont.load_default()

    y = 20
    for line in lines:
        draw.text((20, y), line, fill=text_color, font=font)
        y += 30

    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, f"{job_id}_overlay.png")
    img.save(file_path)
    return file_path
