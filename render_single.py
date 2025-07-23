
import os
import json
import argparse
from datetime import datetime
from pathlib import Path
import random

# ========== CONFIGURATION ========== #
RENDER_OUTPUT_DIR = Path("renders/")
POSE_LOOKUP_FILE = Path("ai_pose_lookup.json")
EXERCISE_REGISTRY_FILE = Path("exercise_registry.json")
METADATA_FILENAME = "metadata.json"
PROMPT_FILENAME = "prompt.txt"

# ========== UTILITIES ========== #
def load_json(filepath):
    if not filepath.exists():
        print(f"[ERROR] File not found: {filepath}")
        return {}
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(data, filepath):
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def write_prompt_file(prompt, path):
    with open(path / PROMPT_FILENAME, "w", encoding="utf-8") as f:
        f.write(prompt)

def generate_prompt(exercise_name, tags, seed):
    return f"Athia Fit character performing {exercise_name}, {', '.join(tags)}, seed={seed}"

# ========== RENDER HANDLER ========== #
def run_render(exercise_name):
    print(f"--- Starting render: {exercise_name} ---")
    registry = load_json(EXERCISE_REGISTRY_FILE)
    pose_lookup = load_json(POSE_LOOKUP_FILE)

    if exercise_name not in registry:
        print(f"[ERROR] Exercise not found in registry: {exercise_name}")
        return

    tags = registry[exercise_name].get("tags", [])
    pose_tags = pose_lookup.get(exercise_name, [])
    seed = random.randint(100000, 999999)

    prompt = generate_prompt(exercise_name, tags + pose_tags, seed)

    # Simulated output folder
    exercise_folder = RENDER_OUTPUT_DIR / exercise_name.replace(" ", "_")
    exercise_folder.mkdir(parents=True, exist_ok=True)

    # Save prompt & metadata
    write_prompt_file(prompt, exercise_folder)
    metadata = {
        "exercise": exercise_name,
        "tags": tags,
        "pose_tags": pose_tags,
        "seed": seed,
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }
    save_json(metadata, exercise_folder / METADATA_FILENAME)

    print(f"[OK] Render data written to {exercise_folder}")
    print(f"Prompt:\n{prompt}")
    print("--- Render complete ---")

# ========== CLI ========== #
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Render a single exercise using metadata.")
    parser.add_argument("exercise_name", type=str, help="Name of the exercise to render")
    args = parser.parse_args()

    run_render(args.exercise_name)

