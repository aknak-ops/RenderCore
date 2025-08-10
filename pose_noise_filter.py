# Script to filter broken or anatomically incorrect AI poses

def filter_bad_poses(pose_data):
    return [p for p in pose_data if is_valid(p)]

def is_valid(p):
    return p.get('limb_count', 0) >= 4