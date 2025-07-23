import shutil
import os

def copy_overlay_assets(job_id, output_dir):
    overlay_src = os.path.join("core", "backend", "mock_pose_data", "sample_pose.json")
    overlay_dest = os.path.join(output_dir, f"{job_id}_pose.json")

    try:
        os.makedirs(output_dir, exist_ok=True)
        shutil.copy2(overlay_src, overlay_dest)
        return overlay_dest
    except Exception as e:
        return f"ERROR copying overlay: {e}"
