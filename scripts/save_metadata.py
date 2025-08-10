
import json
import os
from datetime import datetime

def save_metadata(exercise, tags, pose_tags, seed, folder):
    data = {
        "exercise": exercise,
        "tags": tags,
        "pose_tags": pose_tags,
        "seed": seed,
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }
    path = os.path.join(folder, "metadata.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"[OK] Metadata saved to {path}")
