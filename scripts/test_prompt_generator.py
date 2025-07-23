from core.backend.ai_utils import load_exercise_data, generate_3phase_prompts

dataset = load_exercise_data()
key = input("Enter exercise or move: ").strip()
body_type = input("Enter body type (masculine/feminine): ").strip() or "masculine"
prompts = generate_3phase_prompts(key, dataset, body_type)

if isinstance(prompts, str):
    print(prompts)
else:
    for phase, prompt in prompts.items():
        print(f"\n[{phase.upper()}]\n{prompt}")