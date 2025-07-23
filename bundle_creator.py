
import shutil
import os

def bundle_folder(exercise_name):
    src = os.path.join("renders", exercise_name)
    dst = f"{exercise_name}_bundle.zip"
    shutil.make_archive(exercise_name + "_bundle", "zip", src)
    print(f"[OK] Bundle created: {dst}")

if __name__ == "__main__":
    bundle_folder("Barbell_Bicep_Curl")
