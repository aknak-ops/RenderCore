
import os
import shutil

def init_project(dest_folder):
    base_dirs = ["renders", "render_batches", "logs", "output", "debug", "thumbs", "old", "builds"]
    for d in base_dirs:
        full_path = os.path.join(dest_folder, d)
        os.makedirs(full_path, exist_ok=True)
        with open(os.path.join(full_path, ".gitkeep"), "w") as f:
            f.write("")
    print(f"[OK] RenderCore folder structure created in: {dest_folder}")

if __name__ == "__main__":
    init_project("RenderCore_Project")
