# Scans render folders for corrupted or incomplete files
import os

def scan_folder(folder):
    bad_files = []
    for file in os.listdir(folder):
        if not file.endswith(".png"):
            continue
        if os.path.getsize(os.path.join(folder, file)) < 5000:
            bad_files.append(file)
    return bad_files
