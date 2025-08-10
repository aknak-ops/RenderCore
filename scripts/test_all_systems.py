import os
import subprocess

def run_script(label, command):
    print(f"\n🔧 Running: {label}")
    try:
        subprocess.run(command, check=True, shell=True)
        print(f"✅ {label} completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"❌ {label} failed: {e}")

if __name__ == "__main__":
    scripts = [
        ("Test Render", "python scripts/test_render_runner.py"),
        ("Render Validator", "python scripts/render_integrity_scanner.py"),
        ("Prompt Validator", "python scripts/prompt_validator.py"),
        ("Blur Detector", "python scripts/blur_detector.py"),
        ("Recovery Handler", "python scripts/render_recovery.py"),
        ("Prompt Builder", "python scripts/context_prompt_builder.py"),
        ("Drive Uploader", "python scripts/drive_uploader.py"),
        ("Telegram Bot (Check Only)", "python scripts/telegram_bot_runner.py")
    ]

    for label, cmd in scripts:
        run_script(label, cmd)

    print("\n🎉 System diagnostics complete.")