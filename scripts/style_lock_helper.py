
import json

STYLE_FILE = "style_locks.json"

def save_style(exercise, style_data):
    if os.path.exists(STYLE_FILE):
        with open(STYLE_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = {}
    data[exercise] = style_data
    with open(STYLE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"[OK] Style saved for {exercise}")

if __name__ == "__main__":
    save_style("Barbell Bicep Curl", {"lighting": "studio", "camera": "3/4 angle"})
