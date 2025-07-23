
import json

SEED_FILE = "seed_locks.json"

def save_seed(exercise, seed):
    if os.path.exists(SEED_FILE):
        with open(SEED_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = {}
    data[exercise] = seed
    with open(SEED_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"[OK] Seed saved for {exercise}: {seed}")

if __name__ == "__main__":
    save_seed("Barbell Bicep Curl", 123456)
