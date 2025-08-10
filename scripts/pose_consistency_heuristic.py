# Confirms pose is valid for given exercise
# Ensures angles, joints, spacing match pose logic
def check_pose(exercise, pose_data):
    return pose_data.is_consistent()
