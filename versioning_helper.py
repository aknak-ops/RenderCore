
import os
import shutil

def create_versioned_copy(folder, version="v2"):
    src = os.path.join("renders", folder)
    dst = os.path.join("renders", version, folder)
    if os.path.exists(src):
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copytree(src, dst)
        print(f"[OK] Versioned copy created at {dst}")
    else:
        print("[ERROR] Source folder not found")

if __name__ == "__main__":
    create_versioned_copy("Barbell_Bicep_Curl", "v2")
