def run(prompt):
    max_words = 30
    if len(prompt.split()) > max_words:
        raise ValueError("Prompt too long for length_limiter plugin.")
    return prompt
