import os
from PIL import Image, ImageDraw

def invoke_generate(prompt, job_id, output_dir):
    try:
        img = Image.new("RGB", (512, 512), (0, 0, 0))
        draw = ImageDraw.Draw(img)
        draw.text((20, 240), f"Prompt: {prompt}", fill=(255, 255, 255))

        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, f"{job_id}_invoke.png")
        img.save(output_path)
        return output_path
    except Exception as e:
        return f"ERROR generating image: {e}"
