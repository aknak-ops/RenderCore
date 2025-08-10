import os
def scan(folder):
    print(f"🔍 Scanning: {folder}")
    if not os.path.exists(folder): print("❌ Missing folder."); return
    for file in os.listdir(folder):
        path = os.path.join(folder, file)
        if not file.endswith('.png') or os.path.getsize(path) < 10:
            print(f"❗ Check: {file}")
        else:
            print(f"✅ OK: {file}")
if __name__ == "__main__": scan("output/test_render")