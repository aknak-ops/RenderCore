import os
import json
from PIL import Image, ImageDraw

THEME_MAP_PATH = "theme_gradient_map.json"
OUTPUT_DIR = "theme_swatches"
IMG_WIDTH = 300
IMG_HEIGHT = 100

def draw_gradient(colors, filename):
    img = Image.new("RGB", (IMG_WIDTH, IMG_HEIGHT))
    draw = ImageDraw.Draw(img)
    for x in range(IMG_WIDTH):
        ratio = x / IMG_WIDTH
        left = int(ratio * (len(colors) - 1))
        right = min(left + 1, len(colors) - 1)
        blend = ratio * (len(colors) - 1) - left
        r = int((1 - blend) * colors[left][0] + blend * colors[right][0])
        g = int((1 - blend) * colors[left][1] + blend * colors[right][1])
        b = int((1 - blend) * colors[left][2] + blend * colors[right][2])
        draw.line([(x, 0), (x, IMG_HEIGHT)], fill=(r, g, b))
    img.save(os.path.join(OUTPUT_DIR, filename))

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def main():
    if not os.path.exists(THEME_MAP_PATH):
        print("[!] theme_gradient_map.json not found.")
        return

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    with open(THEME_MAP_PATH, "r") as f:
        themes = json.load(f)

    for theme_name, hex_list in themes.items():
        colors = [hex_to_rgb(h) for h in hex_list]
        filename = f"{theme_name}.png"
        print(f"[+] Generating: {filename}")
        draw_gradient(colors, filename)

if __name__ == "__main__":
    main()
