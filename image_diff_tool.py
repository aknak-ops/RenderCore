
from PIL import ImageChops, Image
import os

def compare_images(img1_path, img2_path, output_path="diff.png"):
    img1 = Image.open(img1_path).convert("RGB")
    img2 = Image.open(img2_path).convert("RGB")
    diff = ImageChops.difference(img1, img2)
    diff.save(output_path)
    print(f"[OK] Diff saved to {output_path}")

if __name__ == "__main__":
    compare_images("renders/Barbell_Bicep_Curl/pose1.png", "renders/Barbell_Bicep_Curl/pose2.png")
