
import csv
import os

def save_prompt_history(exercise, prompt):
    file = "prompt_history.csv"
    write_header = not os.path.exists(file)
    with open(file, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(["exercise", "prompt"])
        writer.writerow([exercise, prompt])
    print(f"[OK] Prompt saved for {exercise}")

if __name__ == "__main__":
    save_prompt_history("Barbell Bicep Curl", "Athia Fit character doing barbell curl with biceps tags")
