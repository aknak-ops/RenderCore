import os
def simulate_render():
    print("🧪 Starting test render...")
    os.makedirs("output/test_render", exist_ok=True)
    with open("output/test_render/frame_001.png", "w") as f:
        f.write("Simulated render output.")
    print("✅ Done: output/test_render/")
if __name__ == "__main__": simulate_render()