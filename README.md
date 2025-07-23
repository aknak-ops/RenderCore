
# RenderCore System

RenderCore is a modular AI render workflow system designed for full-body pose generation, metadata control, QA validation, and structured asset exports. It powers projects like Athia Fit.

---

## 📁 Folder Structure

```
/renders/              → Final image outputs
/render_batches/       → JSON batch configs
/logs/                 → Optional debug logs
/output/               → Rendered zip/exports
/thumbs/               → Grids or strip previews
/old/                  → Archived folders
/builds/               → Final deployment packages
```

---

## 🧠 Core Tools

| Script                  | Description                                |
|-------------------------|--------------------------------------------|
| render_single.py        | Run a single exercise render               |
| render_batch.py         | Batch render from JSON list                |
| rendercore_launcher.py  | CLI control menu                           |
| generate_prompt.py      | Prompt generator utility                   |
| check_pose_errors.py    | Validates missing pose metadata            |

---

## 🧰 Advanced & Validation

| Script                    | Purpose                                  |
|---------------------------|------------------------------------------|
| pose_validator.py         | Checks pose tag balance & missing tags   |
| rerender_incorrect.py     | Reruns renders marked 'retry'            |
| seed_lock_helper.py       | Saves fixed seed per exercise            |
| danger_tag_blocker.py     | Flags unsafe tags                        |
| style_lock_helper.py      | Saves lighting/camera for style match    |
| overlay_pose_preview.py   | Adds skeleton/line overlays to renders   |
| image_classifier_check.py | Stub for matching output with intent     |

---

## 📦 Export, QA, Utility

| Script                    | Purpose                                      |
|---------------------------|----------------------------------------------|
| generate_thumb_grid.py    | 4xN image grid preview                       |
| zip_renders.py            | Zip any `/renders/<exercise>` folder        |
| auto_archive_old.py       | Moves old renders to `/old/`                |
| flag_quality.py           | Mark folders as 'clean'/'retry'/'error'     |
| auto_rename_outputs.py    | Renames all images in folder                |
| versioning_helper.py      | Copies to `/renders/v2/<exercise>`          |
| bundle_creator.py         | Zip render folder into bundle               |
| export_tagger.py          | Adds export_tag.json                        |
| version_tagger.py         | Generates version_tags.json summary         |

---

## 🧹 Maintenance & Tracking

- changelog_tracker.py → appends to `CHANGELOG.txt`
- prompt_history_tracker.py → logs all prompts to CSV
- snap_to_grid_namer.py → grid-aligned image naming
- blur_detector.py → basic blur flagging
- clean_gitkeep.py → removes `.gitkeep` files recursively

---

## 🧾 Metadata Files

- `exercise_registry.json`  
- `ai_pose_lookup.json`  
- `quality_flags.json`  
- `style_locks.json`  
- `seed_locks.json`  
- `build_manifest.json`  
- `version_tags.json`  
- `image_hashes.json`  
- `prompt_history.csv` (generated)  
- `CHANGELOG.txt` (optional)

---

> All scripts are terminal-ready and can be used in isolation or via `rendercore_launcher.py`.
