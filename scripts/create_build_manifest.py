
import os
import json

def create_manifest(root="renders"):
    manifest = []
    for folder in os.listdir(root):
        path = os.path.join(root, folder)
        if os.path.isdir(path):
            files = os.listdir(path)
            manifest.append({
                "exercise": folder,
                "files": files
            })
    with open("build_manifest.json", "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)
    print("[OK] build_manifest.json created")

if __name__ == "__main__":
    create_manifest()
