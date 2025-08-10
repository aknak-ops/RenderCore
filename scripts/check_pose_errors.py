
import os
import json

def check_metadata(folder_path):
    for dirpath, dirnames, filenames in os.walk(folder_path):
        if "metadata.json" in filenames:
            with open(os.path.join(dirpath, "metadata.json"), "r", encoding="utf-8") as f:
                data = json.load(f)
                if not data.get("pose_tags"):
                    print(f"[WARNING] Missing pose_tags: {dirpath}")

if __name__ == "__main__":
    check_metadata("renders")
