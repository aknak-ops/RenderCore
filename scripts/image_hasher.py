
import hashlib
import os
import json

def hash_images(folder="renders"):
    hashes = {}
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith((".png", ".jpg")):
                path = os.path.join(root, file)
                with open(path, "rb") as f:
                    content = f.read()
                file_hash = hashlib.md5(content).hexdigest()
                hashes[path] = file_hash
    with open("image_hashes.json", "w", encoding="utf-8") as f:
        json.dump(hashes, f, indent=2)
    print(f"[OK] Hashed {len(hashes)} images")

if __name__ == "__main__":
    hash_images()
