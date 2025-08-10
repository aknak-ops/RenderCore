def get_default_prompt(path="core/config/default_prompt.txt"):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read().strip()
    except Exception:
        return "Default prompt not available."
