def validate(prompt):
    banned = ["nude", "gore", "violent"]
    for word in banned:
        if word in prompt:
            print(f"❌ Banned tag found: {word}")
            return False
    print("✅ Prompt is safe.")
    return True
if __name__ == "__main__":
    validate("3d muscular male full body white background")