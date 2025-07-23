
import os
import shutil

def archive(folder_name):
    src = os.path.join("renders", folder_name)
    dst = os.path.join("old", folder_name)
    if os.path.exists(src):
        shutil.move(src, dst)
        print(f"[OK] Archived {folder_name}")
    else:
        print("[ERROR] Folder not found")

if __name__ == "__main__":
    archive("Barbell_Bicep_Curl")
