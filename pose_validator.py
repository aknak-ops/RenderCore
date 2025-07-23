
import json
import os

def validate_poses(folder="renders"):
    for root, dirs, files in os.walk(folder):
        if "metadata.json" in files:
            path = os.path.join(root, "metadata.json")
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            issues = []
            if not data.get("pose_tags"):
                issues.append("Missing pose_tags")
            if "arms" in str(data.get("pose_tags", [])).lower() and "legs" not in str(data.get("pose_tags", [])).lower():
                issues.append("Upper body imbalance")
            if issues:
                print(f"[!] Issue in {root}: {', '.join(issues)}")

if __name__ == "__main__":
    validate_poses()
