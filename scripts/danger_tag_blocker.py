
def check_dangerous_tags(tags):
    banned = {"nude", "weapon", "blood", "gore"}
    if any(tag in banned for tag in tags):
        return True
    return False

if __name__ == "__main__":
    print(check_dangerous_tags(["nude", "barbell"]))
