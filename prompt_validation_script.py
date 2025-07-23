
def validate_prompt(prompt):
    banned = ["nude", "explosion"]
    for word in banned:
        if word in prompt.lower():
            return False
    return True

if __name__ == "__main__":
    test = "Athia Fit character doing explosion jump"
    print("Prompt valid?" , validate_prompt(test))
