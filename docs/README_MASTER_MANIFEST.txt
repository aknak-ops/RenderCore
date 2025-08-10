
==============================
ATHIA FIT / RENDERCORE SYSTEM
==============================

This folder contains the full RenderCore system including:

📁 CORE RENDERING
- render_single.py
- render_batch.py
- generate_prompt.py
- save_metadata.py
- rendercore_launcher.py
- ai_pose_lookup.json
- exercise_registry.json

📁 QA + VALIDATION
- check_pose_errors.py
- pose_validator.py
- image_classifier_check.py
- rerender_incorrect.py
- seed_lock_helper.py
- style_lock_helper.py
- danger_tag_blocker.py
- prompt_validation_script.py
- overlay_pose_preview.py
- image_diff_tool.py
- blur_detector.py

📁 EXPORT + UTILITY
- flag_quality.py
- zip_renders.py
- create_build_manifest.py
- versioning_helper.py
- export_tagger.py
- version_tagger.py
- bundle_creator.py
- auto_archive_old.py
- auto_rename_outputs.py
- changelog_tracker.py
- prompt_history_tracker.py
- snap_to_grid_namer.py
- clean_gitkeep.py

📁 FRONTEND UI (Web + Electron)
- web_ui/index.html
- web_ui_backend/app.py
- electron_app/main.js
- electron_app/index.html
- electron_app/package.json

📁 CLOUD SYNC (Google Drive)
- drive_auth.py
- upload_to_drive.py
- create_drive_folder.py

📁 REMOTE TRIGGERING
- remote_trigger_server.py
- test_trigger_request.py

📁 SYSTEM METADATA
- quality_flags.json
- seed_locks.json
- style_locks.json
- build_manifest.json
- version_tags.json
- image_hashes.json
- prompt_history.csv
- CHANGELOG.txt

All folders contain .gitkeep or placeholders to preserve structure.

TO RUN: See `README.md` or launcher script.
