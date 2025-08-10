import tkinter as tk
import subprocess
from tkinter import messagebox

def open_project():
    messagebox.showinfo("Opening VS Code", "Launching RenderCore project...")
    subprocess.Popen(["code", "D:/RenderCore/rendercore_bundle/RenderCore"])

def run_batch():
    messagebox.showinfo("Running Batch", "Render batch triggered!")

def show_settings():
    messagebox.showinfo("Settings", "Settings panel coming soon.")

root = tk.Tk()
root.title("RenderCore Launcher")
root.geometry("480x600")
root.configure(bg="#121212")

tk.Label(root, text="Select Project", fg="white", bg="#121212", font=("Arial", 16)).pack(pady=10)

projects = ["Athia Fit"]
systems = {"Athia Fit": ["Characters", "UI"]}

selected_project = tk.StringVar(value=projects[0])
selected_system = tk.StringVar(value=systems[projects[0]][0])

def update_system_menu(*args):
    menu = system_menu["menu"]
    menu.delete(0, "end")
    for system in systems[selected_project.get()]:
        menu.add_command(label=system, command=tk._setit(selected_system, system))

tk.OptionMenu(root, selected_project, *projects, command=update_system_menu).pack(pady=5)
system_menu = tk.OptionMenu(root, selected_system, *systems[projects[0]])
system_menu.pack(pady=5)

tk.Button(root, text="Launch VS Code", command=open_project, width=25).pack(pady=10)
tk.Button(root, text="Run Render Batch", command=run_batch, width=25).pack(pady=5)
tk.Button(root, text="Settings", command=show_settings, width=25).pack(pady=5)

tk.Label(root, text="Resource Usage", fg="white", bg="#121212", font=("Arial", 14)).pack(pady=20)
tk.Label(root, text="[CPU / GPU / RAM Placeholder]", fg="#00FF88", bg="#121212", font=("Consolas", 12)).pack()

root.mainloop()
