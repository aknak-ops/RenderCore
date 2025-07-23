
import os
import json
import argparse
from render_single import run_render

RENDER_BATCHES_DIR = "render_batches"

def load_batch(batch_file):
    with open(batch_file, "r", encoding="utf-8") as f:
        return json.load(f)

def run_batch(batch_name):
    path = os.path.join(RENDER_BATCHES_DIR, batch_name + ".json")
    if not os.path.exists(path):
        print(f"[ERROR] Batch not found: {path}")
        return
    batch = load_batch(path)
    for exercise in batch.get("exercises", []):
        run_render(exercise)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("batch_name", help="Name of the batch JSON (without .json)")
    args = parser.parse_args()
    run_batch(args.batch_name)
