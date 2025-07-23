
import os
import shutil

def clean_folder(path, keyword="bad"):
    if not os.path.exists(path):
        print(f"No folder: {path}")
        return
    removed = 0
    for dirpath, dirs, files in os.walk(path):
        for d in dirs:
            if keyword in d:
                full_path = os.path.join(dirpath, d)
                shutil.rmtree(full_path)
                print(f"[REMOVED] {full_path}")
                removed += 1
    print(f"Done. Removed {removed} folders.")

if __name__ == "__main__":
    clean_folder("renders", keyword="bad")
