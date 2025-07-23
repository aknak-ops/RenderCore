
import json

def build():
    synonyms = {
        "bicep curls": "Barbell Bicep Curl",
        "push ups": "Push-Up",
        "lunges": "Lunge",
        "pull ups": "Pull-Up",
        "squat jump": "Jump Squat"
    }
    with open("search_alias_map.json", "w", encoding="utf-8") as f:
        json.dump(synonyms, f, indent=2)
    print("[OK] Synonym map written to search_alias_map.json")

if __name__ == "__main__":
    build()
