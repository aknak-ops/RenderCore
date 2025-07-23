
import os
import shutil
from zipfile import ZipFile

def zip_folder(folder_name):
    path = os.path.join("renders", folder_name)
    zip_path = f"{folder_name}.zip"
    with ZipFile(zip_path, "w") as zipf:
        for root, dirs, files in os.walk(path):
            for file in files:
                full = os.path.join(root, file)
                arc = os.path.relpath(full, "renders")
                zipf.write(full, arc)
    print(f"[OK] Zipped to {zip_path}")

if __name__ == "__main__":
    zip_folder("Barbell_Bicep_Curl")
