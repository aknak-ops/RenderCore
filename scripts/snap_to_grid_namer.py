
import os

def rename_gridwise(folder):
    files = sorted(f for f in os.listdir(folder) if f.endswith(".png"))
    for i, file in enumerate(files):
        new_name = f"grid_{i // 4 + 1}_{i % 4 + 1}.png"
        os.rename(os.path.join(folder, file), os.path.join(folder, new_name))
    print(f"[OK] Renamed {len(files)} images to grid format.")

if __name__ == "__main__":
    rename_gridwise("renders/Barbell_Bicep_Curl")
