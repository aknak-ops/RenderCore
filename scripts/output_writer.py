import os

def save_render_output(output_dir, job_id, content):
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, f"{job_id}_output.txt")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    return file_path
