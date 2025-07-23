
from PIL import Image, ImageFilter
import os

def is_blurry(image_path, threshold=100.0):
    img = Image.open(image_path).convert("L")
    variance = img.filter(ImageFilter.FIND_EDGES).variance()
    return variance < threshold

def check_blur(folder="renders"):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".png"):
                full = os.path.join(root, file)
                try:
                    if is_blurry(full):
                        print(f"[BLUR] {full}")
                except Exception:
                    pass

if __name__ == "__main__":
    check_blur()
