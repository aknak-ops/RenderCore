import os
import uuid
from datetime import datetime
from backend.ai_utils import load_exercise_data, generate_3phase_prompts

def save_render_output(output_dir, job_id, phase, content):
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, f"{job_id}_{phase}.txt")
    with open(file_path, "w") as f:
        f.write(content)
    return file_path

def main():
    job_id = str(uuid.uuid4())[:8]
    job_name = input("Enter job name (must match dataset key for 3-phase AI): ").strip()
    body_type = input("Body type (masculine/feminine): ").strip() or "masculine"

    dataset = load_exercise_data()
    prompts = generate_3phase_prompts(job_name, dataset, body_type)

    if isinstance(prompts, str):
        print(f"Standard prompt used: {job_name}")
        save_render_output("output", job_id, "main", job_name)
    else:
        print("3-phase AI prompt generated:")
        for phase, prompt in prompts.items():
            print(f"\n[{phase.upper()}]\n{prompt}")
            save_render_output("output", job_id, phase, prompt)

    print(f"Render job {job_id} completed. Files saved to /output.")

if __name__ == "__main__":
    main()