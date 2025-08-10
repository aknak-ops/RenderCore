from PIL import Image, ImageFilter
import os

def detect_blur(folder="output/"):
    print(f"🔍 Scanning for blurry images in {folder}")
    for root, _, files in os.walk(folder):
        for f in files:
            if f.endswith(".png"):
                path = os.path.join(root, f)
                try:
                    img = Image.open(path).convert("L")
                    score = img.filter(ImageFilter.FIND_EDGES).getbbox()
                    if score is None:
                        print(f"⚠️ Possibly blurry: {path}")
                except Exception as e:
                    print(f"❌ Error reading {path}: {e}")
if __name__ == "__main__":
    detect_blur()