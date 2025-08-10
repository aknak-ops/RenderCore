
import os

def menu():
    print("\nRenderCore Master Launcher")
    print("==========================")
    print("1. Run single render")
    print("2. Run batch render")
    print("3. Check pose metadata")
    print("4. Re-render failed entries")
    print("5. Generate thumbnail grid")
    print("6. Flag render quality")
    print("7. Zip render folder")
    print("8. Save prompt history")
    print("9. Archive to /old/")
    print("10. Exit")

def run():
    while True:
        menu()
        choice = input("Select an option: ")
        if choice == "1":
            name = input("Exercise name: ")
            os.system(f"python render_single.py \"{name}\"")
        elif choice == "2":
            name = input("Batch name: ")
            os.system(f"python render_batch.py {name}")
        elif choice == "3":
            os.system("python check_pose_errors.py")
        elif choice == "4":
            os.system("python rerender_incorrect.py")
        elif choice == "5":
            folder = input("Folder name: ")
            os.system(f"python generate_thumb_grid.py {folder}")
        elif choice == "6":
            name = input("Exercise folder: ")
            flag = input("Flag (clean/retry/error): ")
            os.system(f"python flag_quality.py {name} {flag}")
        elif choice == "7":
            name = input("Folder to zip: ")
            os.system(f"python zip_renders.py {name}")
        elif choice == "8":
            name = input("Exercise: ")
            prompt = input("Prompt: ")
            os.system(f"python prompt_history_tracker.py \"{name}\" \"{prompt}\"")
        elif choice == "9":
            name = input("Folder name: ")
            os.system(f"python auto_archive_old.py {name}")
        elif choice == "10":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run()
