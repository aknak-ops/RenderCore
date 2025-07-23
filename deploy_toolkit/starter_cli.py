
import os

def menu():
    print("\n[RenderCore CLI Launcher]")
    print("1. Run render (single)")
    print("2. Run batch")
    print("3. Check poses")
    print("4. Retry failed")
    print("5. Build manifest")
    print("6. Exit")

def run():
    while True:
        menu()
        choice = input(">> ")
        if choice == "1":
            e = input("Exercise: ")
            os.system(f"python render_single.py \"{e}\"")
        elif choice == "2":
            b = input("Batch: ")
            os.system(f"python render_batch.py {b}")
        elif choice == "3":
            os.system("python check_pose_errors.py")
        elif choice == "4":
            os.system("python rerender_incorrect.py")
        elif choice == "5":
            os.system("python create_build_manifest.py")
        elif choice == "6":
            break

if __name__ == "__main__":
    run()
