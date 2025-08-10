import psutil

def get_status():
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    return f"CPU Usage: {cpu}%\nRAM Usage: {ram}%"
