
import json

def check_version():
    with open("version.json", "r", encoding="utf-8") as f:
        v = json.load(f)
    print(f"🔄 RenderCore Version: {v['rendercore_version']} — Last Updated: {v['last_updated']}")

if __name__ == "__main__":
    check_version()
