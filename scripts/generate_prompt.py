
def generate_prompt(exercise_name, tags, seed):
    return f"Athia Fit character performing {exercise_name}, {', '.join(tags)}, seed={seed}"

if __name__ == "__main__":
    sample = generate_prompt("Push-Up", ["bodyweight", "chest", "strength"], 123456)
    print(sample)
