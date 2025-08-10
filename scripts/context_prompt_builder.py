import json

def build_prompt(pose):
    prompt = f"{pose['name']}, camera angle: {pose.get('camera', '3/4 front')}, theme: {pose.get('theme', 'Steel Fade')}, anatomical style, clean white background"
    return prompt

def run_batch(file="render_batches/test_batch.json"):
    with open(file, "r") as f:
        data = json.load(f)
    for pose in data["poses"]:
        print(f"🧠 Prompt: {build_prompt(pose)}")

if __name__ == "__main__":
    run_batch()