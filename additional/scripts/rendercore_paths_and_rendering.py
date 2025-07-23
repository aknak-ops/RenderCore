import os
import json
import argparse
from datetime import datetime
import random
from pathlib import Path

# Root folders for exercise categories
CATEGORY_ROOTS = {
    "workout": "workout",
    "stretch": "stretch",
    "fight": "fight",
    "yoga": "yoga"
}

# Base render output folder
RENDER_OUTPUT_BASE = Path("renders")

# Registry file with category and tags
EXERCISE_REGISTRY_FILE = Path("additional/metadata/exercise_registry.json")

def load_registry():
    if not EXERCISE_REGISTRY_FILE.exists():
        raise FileNotFoundError(f"Registry file not found: {EXERCISE_REGISTRY_FILE}")
    with open(EXERCISE_REGISTRY_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def get_exercise_path(category, exercise_name):
    category_folder = CATEGORY_ROOTS.get(category)
    if not category_folder:
        raise ValueError(f"Unknown category: {category}")
    return Path(category_folder) / exercise_name

def generate_prompt(exercise_name, tags, seed, include_muscle_map):
    base_prompt = f"Athia Fit character performing {exercise_name}, {', '.join(tags)}, seed={seed}"
    if include_muscle_map:
        base_prompt += ", with muscle maps highlighting targeted muscles"
    return base_prompt

def run_render(category, exercise_name):
    print(f"--- Starting render: {exercise_name} in category {category} ---")

    registry = load_registry()
    exercise_key = exercise_name.lower().replace(" ", "_")

    if exercise_key not in registry:
        print(f"[ERROR] Exercise not found in registry: {exercise_key}")
        return

    exercise_data = registry[exercise_key]
    tags = exercise_data.get("tags", [])
    seed = random.randint(100000, 999999)

    # Determine if muscle maps should be included (only for workout)
    include_muscle_map = (category == "workout")

    prompt = generate_prompt(exercise_name, tags, seed, include_muscle_map)

    exercise_folder = get_exercise_path(category, exercise_key)
    output_folder = RENDER_OUTPUT_BASE / exercise_folder
    output_folder.mkdir(parents=True, exist_ok=True)

    # Save prompt
    prompt_file = output_folder / "prompt.txt"
    with open(prompt_file, "w", encoding="utf-8") as f:
        f.write(prompt)

    # Prepare metadata
    metadata = {
        "exercise": exercise_key,
        "category": category,
        "tags": tags,
        "seed": seed,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "include_muscle_map": include_muscle_map
    }

    # Optionally, save muscle map paths if applicable
    if include_muscle_map:
        metadata["muscle_map_front"] = str(output_folder / "muscle_map_front.png")
        metadata["muscle_map_back"] = str(output_folder / "muscle_map_back.png")

    metadata_file = output_folder / "metadata.json"
    with open(metadata_file, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)

    print(f"[OK] Render data written to {output_folder}")
    print(f"Prompt:\n{prompt}")
    print("--- Render complete ---")

def run_batch(batch_file):
    if not Path(batch_file).exists():
        print(f"[ERROR] Batch file not found: {batch_file}")
        return
    with open(batch_file, "r", encoding="utf-8") as f:
        batch = json.load(f)

    for item in batch.get("exercises", []):
        category = item.get("category")
        name = item.get("name")
        if not category or not name:
            print(f"[WARNING] Batch item missing category or name: {item}")
            continue
        run_render(category, name)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="RenderCore updated render script with muscle map handling")
    parser.add_argument("--category", type=str, help="Exercise category (workout/stretch/fight/yoga)")
    parser.add_argument("--exercise", type=str, help="Exercise name")
    parser.add_argument("--batch", type=str, help="Path to batch JSON")
    args = parser.parse_args()

    if args.batch:
        run_batch(args.batch)
    elif args.category and args.exercise:
        run_render(args.category, args.exercise)
    else:
        print("Usage:")
        print("  python rendercore_paths_and_rendering.py --category workout --exercise dumbbell_bicep_curl")
        print("  python rendercore_paths_and_rendering.py --batch additional/render_batches/test_batch.json")
