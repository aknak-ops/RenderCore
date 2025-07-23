
import os

def remove_gitkeep(folder="."):
    removed = 0
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file == ".gitkeep":
                os.remove(os.path.join(root, file))
                removed += 1
    print(f"[OK] Removed {removed} .gitkeep files")

if __name__ == "__main__":
    remove_gitkeep()
