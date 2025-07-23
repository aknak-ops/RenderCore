import os

def get_env_flag(name, default="false"):
    return os.getenv(name, default).lower() == "true"

def get_env_value(name, default):
    return os.getenv(name, default)
