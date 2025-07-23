
import json
import os
from render_single import run_render

def rerender_all(flag_file="quality_flags.json"):
    with open(flag_file, "r", encoding="utf-8") as f:
        flags = json.load(f)

    for name, status in flags.items():
        if status == "retry":
            print(f"[RETRY] Re-rendering: {name}")
            run_render(name)

if __name__ == "__main__":
    rerender_all()
