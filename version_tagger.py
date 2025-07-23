
import os
import json

def tag_versions(root="renders"):
    tags = {}
    for folder in os.listdir(root):
        version_file = os.path.join(root, folder, "export_tag.json")
        if os.path.exists(version_file):
            with open(version_file, "r", encoding="utf-8") as f:
                tag = json.load(f)
            tags[folder] = tag.get("version", "v1")
    with open("version_tags.json", "w", encoding="utf-8") as f:
        json.dump(tags, f, indent=2)
    print("[OK] version_tags.json created")

if __name__ == "__main__":
    tag_versions()
