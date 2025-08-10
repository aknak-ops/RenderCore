def extract_tags(prompt):
    """
    Extracts --tag or --tags from the prompt string.
    Example: "run fast --tag quick --tag speed" → ["quick", "speed"]
    """
    tags = []
    parts = prompt.split("--tag")
    for part in parts[1:]:
        tag = part.strip().split()[0]
        tags.append(tag)
    return tags
