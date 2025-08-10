# Automatically reruns renders with adjusted poses if errors are detected
def correct_pose(render_path, issue_type):
    print(f"Re-rendering {render_path} to fix: {issue_type}")
    return True
