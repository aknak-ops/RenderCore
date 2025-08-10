
from PIL import Image, ImageDraw
import os

def draw_overlay(image_path, output_path):
    img = Image.open(image_path).convert("RGB")
    draw = ImageDraw.Draw(img)
    w, h = img.size
    draw.line((w*0.5, 0, w*0.5, h), fill="red", width=2)
    draw.line((0, h*0.5, w, h*0.5), fill="blue", width=2)
    img.save(output_path)
    print(f"[OK] Overlay saved: {output_path}")

if __name__ == "__main__":
    draw_overlay("renders/Barbell_Bicep_Curl/pose1.png", "renders/Barbell_Bicep_Curl/overlay_preview.png")
