
import os

def menu():
    print("\nRenderCore Launcher")
    print("====================")
    print("1. Run single render")
    print("2. Run batch render")
    print("3. Check pose errors")
    print("4. Exit")

def run():
    while True:
        menu()
        choice = input("Select an option: ")
        if choice == "1":
            name = input("Enter exercise name: ")
            os.system(f"python render_single.py \"{name}\"")
        elif choice == "2":
            batch = input("Enter batch name: ")
            os.system(f"python render_batch.py {batch}")
        elif choice == "3":
            os.system("python check_pose_errors.py")
        elif choice == "4":
            print("Exiting.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run()
