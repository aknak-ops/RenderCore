
import datetime

def add_changelog(message):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("CHANGELOG.txt", "a", encoding="utf-8") as f:
        f.write(f"[{now}] {message}\n")
    print("[OK] Log added.")

if __name__ == "__main__":
    add_changelog("Added final polish phase tools.")
