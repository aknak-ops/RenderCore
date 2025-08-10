
import json
import os

def validate_registry(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for key, value in data.items():
            if not isinstance(value, dict) or 'tags' not in value:
                print(f"[ERROR] Invalid entry for: {key}")
            else:
                print(f"[OK] {key}")
    except Exception as e:
        print(f"[FAIL] Could not parse {file_path}: {e}")

if __name__ == "__main__":
    validate_registry("exercise_registry.json")
