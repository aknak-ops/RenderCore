def is_pose_valid(pose_json):
    return "keypoints" in pose_json and len(pose_json["keypoints"]) > 0
