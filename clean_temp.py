
import os

def delete_temp_files(folder):
    count = 0
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".tmp") or file.startswith("temp_"):
                full = os.path.join(root, file)
                os.remove(full)
                print(f"Deleted {full}")
                count += 1
    print(f"{count} temp files deleted.")

if __name__ == "__main__":
    delete_temp_files("renders")
