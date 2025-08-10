
import json
import os

def generate_labels(path="renders", output="labels.json"):
    labels = {}
    for folder in os.listdir(path):
        fpath = os.path.join(path, folder)
        if os.path.isdir(fpath):
            labels[folder] = [f"pose{i+1}" for i in range(3)]
    with open(output, "w", encoding="utf-8") as f:
        json.dump(labels, f, indent=2)
    print(f"[OK] labels.json created")

if __name__ == "__main__":
    generate_labels()
