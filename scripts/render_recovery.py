import os
def recover_failed():
    output_dir = "output/"
    failures = []
    for root, dirs, files in os.walk(output_dir):
        if not any(f.endswith(".png") for f in files):
            failures.append(root)
    if not failures:
        print("✅ No missing renders found.")
    else:
        print("🔁 Recovery triggered for:")
        for f in failures:
            print(f" - {f}")
if __name__ == "__main__":
    recover_failed()