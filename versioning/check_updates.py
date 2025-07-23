
import json
import requests

LOCAL_FILE = "version.json"
REMOTE_URL = "https://example.com/rendercore/version.json"  # Replace with your URL later

def load_local():
    with open(LOCAL_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def fetch_remote():
    try:
        response = requests.get(REMOTE_URL, timeout=5)
        return response.json()
    except Exception as e:
        print("[ERROR] Could not fetch remote version.")
        return None

def compare_versions(local, remote):
    if not remote:
        return
    if remote["rendercore_version"] != local["rendercore_version"]:
        print(f"[UPDATE AVAILABLE] New version: {remote['rendercore_version']}")
        for change in remote.get("changelog", []):
            print(" -", change)
    else:
        print("[OK] You are on the latest version.")

if __name__ == "__main__":
    local = load_local()
    remote = fetch_remote()
    compare_versions(local, remote)
