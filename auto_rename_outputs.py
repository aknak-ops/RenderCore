
import os

def rename_images(folder):
    files = sorted([f for f in os.listdir(folder) if f.endswith(('.png', '.jpg'))])
    for i, file in enumerate(files):
        ext = os.path.splitext(file)[1]
        new_name = f"frame_{i+1:02d}{ext}"
        os.rename(os.path.join(folder, file), os.path.join(folder, new_name))
    print(f"Renamed {len(files)} files in {folder}")

if __name__ == "__main__":
    rename_images("renders/Barbell_Bicep_Curl")
