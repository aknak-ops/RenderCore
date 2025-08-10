
import json
import os

def tag_export(folder, version="v1", author="system", notes=""):
    tag = {
        "exercise": folder,
        "version": version,
        "author": author,
        "notes": notes
    }
    out = os.path.join("renders", folder, "export_tag.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(tag, f, indent=2)
    print(f"[OK] Export tag saved: {out}")

if __name__ == "__main__":
    tag_export("Barbell_Bicep_Curl", notes="Initial AI render pass")
