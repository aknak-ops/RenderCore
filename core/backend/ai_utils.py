import json
import os

def load_exercise_data(path="core/backend/ai_exercise_bank.json"):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return {}

def generate_3phase_prompts(entry_key, dataset, body_type="masculine"):
    entry = dataset.get(entry_key)
    if not entry:
        return f"'{entry_key}' not found in dataset."

    requires_partner = entry.get("requires_partner", False)
    base_style = "muscular fitness figure, {} body type".format(body_type)
    partner_style = "dark orange silhouette, black muscle lines, {} build".format(body_type)

    prompts = {}
    for phase, description in entry.get("phases", {}).items():
        if requires_partner:
            prompt = (
                f"{base_style} performing '{entry_key}' ({phase} phase), "
                f"with a second figure: {partner_style}, clearly showing technique"
            )
        else:
            prompt = f"{base_style} performing '{entry_key}' ({phase} phase), {description}"

        prompts[phase] = prompt

    return prompts