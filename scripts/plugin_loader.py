import importlib
import os

def load_plugins(plugin_dir="core/backend/plugins"):
    plugins = {}
    for filename in os.listdir(plugin_dir):
        if filename.endswith(".py"):
            name = filename[:-3]
            try:
                module = importlib.import_module(f"core.backend.plugins.{name}")
                plugins[name] = module.run
            except Exception as e:
                print(f"⚠️ Failed to load plugin {name}: {e}")
    return plugins
