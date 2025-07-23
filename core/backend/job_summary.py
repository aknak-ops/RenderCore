import json
import os
from datetime import datetime

def save_summary(summary_data, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    summary_data["generated_at"] = datetime.now().isoformat()
    path = os.path.join(output_dir, "summary.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(summary_data, f, indent=2)
    return path
