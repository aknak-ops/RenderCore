def route_plugin(entry):
    prompt = (entry.get("prompt") or "").lower()
    job_id = int(entry.get("id", "0"))

    if "fitness" in prompt:
        return "fitness_enhancer"
    if "debug" in prompt:
        return "debug_logger"
    if "overlay" in prompt:
        return "overlay_generator"
    if job_id % 2 == 0:
        return "default"
    else:
        return "mock_image"
