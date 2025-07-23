
import json
import os

FLAGS_FILE = "quality_flags.json"

def flag(folder_name, flag):
    if os.path.exists(FLAGS_FILE):
        with open(FLAGS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = {}

    data[folder_name] = flag
    with open(FLAGS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"[OK] Flagged {folder_name} as {flag}")

if __name__ == "__main__":
    flag("Barbell_Bicep_Curl", "clean")
