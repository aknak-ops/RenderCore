#!/usr/bin/env python3
"""
RenderCore Stable Diffusion Pipeline
Scans for retry_flag.txt files and generates missing PNG phases using AUTOMATIC1111 API.
"""

import os
import sys
import json
import time
import argparse
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any, Optional

try:
    import requests
except ImportError:
    print("ERROR: requests module not found. Please install with: pip install requests")
    sys.exit(1)


class RenderPipeline:
    def __init__(self, config_path: str = "render_config.json"):
        self.config = self.load_config(config_path)
        self.log_file = Path("generated_pngs") / "render_log.txt"
        self.log_file.parent.mkdir(exist_ok=True)
        self.stats = {
            "folders_processed": 0,
            "images_generated": 0,
            "errors": 0,
            "skipped": 0
        }
        
    def load_config(self, config_path: str) -> Dict[str, Any]:
        """Load configuration from JSON file."""
        default_config = {
            "base_url": "http://127.0.0.1:7860",
            "timeout_sec": 60,
            "retries": 3,
            "backoff_sec": 2,
            "default_phases": 3
        }
        
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
                # Merge with defaults
                for key, value in default_config.items():
                    if key not in config:
                        config[key] = value
                return config
        except FileNotFoundError:
            print(f"WARNING: Config file {config_path} not found. Using defaults.")
            return default_config
        except json.JSONDecodeError as e:
            print(f"ERROR: Invalid JSON in {config_path}: {e}")
            return default_config

    def log_message(self, message: str, print_also: bool = True):
        """Write message to log file and optionally print."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {message}\n"
        
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(log_entry)
        
        if print_also:
            print(message)

    def find_retry_folders(self, scan_paths: List[str]) -> List[Path]:
        """Recursively find folders containing retry_flag.txt."""
        retry_folders = []
        
        for scan_path in scan_paths:
            if not os.path.exists(scan_path):
                self.log_message(f"WARNING: Scan path does not exist: {scan_path}")
                continue
                
            for root, dirs, files in os.walk(scan_path):
                if "retry_flag.txt" in files:
                    retry_folders.append(Path(root))
        
        return retry_folders

    def get_missing_phases(self, folder: Path, num_phases: int) -> List[str]:
        """Determine which phase PNGs are missing."""
        missing_phases = []
        
        for phase_num in range(1, num_phases + 1):
            base_filename = f"phase{phase_num}.png"
            if not (folder / base_filename).exists():
                missing_phases.append(base_filename)
        
        return missing_phases

    def get_versioned_filename(self, folder: Path, base_filename: str) -> str:
        """Get next available versioned filename if base exists."""
        base_path = folder / base_filename
        if not base_path.exists():
            return base_filename
        
        # Find next version number
        name_without_ext = base_filename.replace('.png', '')
        version = 2
        while True:
            versioned_name = f"{name_without_ext}_v{version}.png"
            if not (folder / versioned_name).exists():
                return versioned_name
            version += 1

    def read_prompt_file(self, folder: Path) -> Optional[str]:
        """Read prompt.txt from folder."""
        prompt_file = folder / "prompt.txt"
        if not prompt_file.exists():
            self.log_message(f"WARNING: No prompt.txt found in {folder}")
            return None
        
        try:
            with open(prompt_file, 'r', encoding='utf-8') as f:
                return f.read().strip()
        except Exception as e:
            self.log_message(f"ERROR: Could not read prompt from {prompt_file}: {e}")
            return None

    def call_automatic1111_api(self, prompt: str) -> Optional[bytes]:
        """Call AUTOMATIC1111 txt2img API and return image bytes."""
        url = f"{self.config['base_url']}/sdapi/v1/txt2img"
        
        payload = {
            "prompt": prompt,
            "steps": 20,
            "width": 512,
            "height": 512,
            "cfg_scale": 7,
            "sampler_name": "Euler a"
        }
        
        for attempt in range(self.config['retries']):
            try:
                response = requests.post(
                    url, 
                    json=payload, 
                    timeout=self.config['timeout_sec']
                )
                
                if response.status_code == 200:
                    result = response.json()
                    if 'images' in result and result['images']:
                        # Decode base64 image
                        import base64
                        image_data = base64.b64decode(result['images'][0])
                        return image_data
                    else:
                        self.log_message(f"ERROR: No images in API response")
                        return None
                else:
                    self.log_message(f"ERROR: API returned status {response.status_code}: {response.text}")
                    
            except requests.exceptions.Timeout:
                self.log_message(f"WARNING: API timeout on attempt {attempt + 1}")
            except requests.exceptions.ConnectionError:
                self.log_message(f"WARNING: Connection error on attempt {attempt + 1}")
            except Exception as e:
                self.log_message(f"ERROR: API call failed: {e}")
            
            if attempt < self.config['retries'] - 1:
                time.sleep(self.config['backoff_sec'] * (attempt + 1))
        
        return None

    def save_image(self, image_data: bytes, file_path: Path) -> bool:
        """Save image data to file."""
        try:
            with open(file_path, 'wb') as f:
                f.write(image_data)
            return True
        except Exception as e:
            self.log_message(f"ERROR: Could not save image to {file_path}: {e}")
            return False

    def process_folder(self, folder: Path, dry_run: bool = False) -> bool:
        """Process a single folder with retry_flag.txt."""
        self.log_message(f"Processing folder: {folder}")
        
        # Read prompt
        prompt = self.read_prompt_file(folder)
        if not prompt:
            self.stats["errors"] += 1
            return False
        
        # Check what phases are missing
        missing_phases = self.get_missing_phases(folder, self.config['default_phases'])
        
        if not missing_phases:
            self.log_message(f"SKIP: All phases exist in {folder}")
            self.stats["skipped"] += 1
            return True
        
        self.log_message(f"Missing phases: {missing_phases}")
        
        if dry_run:
            self.log_message(f"DRY-RUN: Would generate {len(missing_phases)} images for: {prompt[:50]}...")
            return True
        
        # Generate missing images
        success = True
        for phase_filename in missing_phases:
            final_filename = self.get_versioned_filename(folder, phase_filename)
            self.log_message(f"Generating: {final_filename}")
            
            image_data = self.call_automatic1111_api(prompt)
            if image_data:
                file_path = folder / final_filename
                if self.save_image(image_data, file_path):
                    self.log_message(f"SUCCESS: Saved {file_path}")
                    self.stats["images_generated"] += 1
                else:
                    success = False
                    self.stats["errors"] += 1
            else:
                self.log_message(f"ERROR: Failed to generate image for {phase_filename}")
                success = False
                self.stats["errors"] += 1
        
        return success

    def remove_retry_flag(self, folder: Path):
        """Remove retry_flag.txt file."""
        retry_flag = folder / "retry_flag.txt"
        try:
            retry_flag.unlink()
            self.log_message(f"Removed retry flag: {retry_flag}")
        except Exception as e:
            self.log_message(f"WARNING: Could not remove retry flag {retry_flag}: {e}")

    def run(self, scan_paths: List[str], dry_run: bool = False, limit: Optional[int] = None):
        """Main pipeline execution."""
        start_time = datetime.now()
        self.log_message(f"=== RenderCore Pipeline Started ===")
        self.log_message(f"Scan paths: {scan_paths}")
        self.log_message(f"Dry run: {dry_run}")
        self.log_message(f"Limit: {limit}")
        
        # Find folders with retry flags
        retry_folders = self.find_retry_folders(scan_paths)
        self.log_message(f"Found {len(retry_folders)} folders with retry flags")
        
        if limit:
            retry_folders = retry_folders[:limit]
            self.log_message(f"Limited to first {limit} folders")
        
        # Process each folder
        for i, folder in enumerate(retry_folders, 1):
            self.log_message(f"--- Processing {i}/{len(retry_folders)}: {folder} ---")
            
            success = self.process_folder(folder, dry_run)
            self.stats["folders_processed"] += 1
            
            if success and not dry_run:
                self.remove_retry_flag(folder)
        
        # Print final summary
        duration = datetime.now() - start_time
        self.log_message(f"=== Pipeline Complete ===")
        self.log_message(f"Duration: {duration}")
        self.log_message(f"Folders processed: {self.stats['folders_processed']}")
        self.log_message(f"Images generated: {self.stats['images_generated']}")
        self.log_message(f"Errors: {self.stats['errors']}")
        self.log_message(f"Skipped: {self.stats['skipped']}")
        
        print(f"\n=== FINAL SUMMARY ===")
        print(f"Duration: {duration}")
        print(f"Folders processed: {self.stats['folders_processed']}")
        print(f"Images generated: {self.stats['images_generated']}")
        print(f"Errors: {self.stats['errors']}")
        print(f"Skipped: {self.stats['skipped']}")


def main():
    parser = argparse.ArgumentParser(description="RenderCore Stable Diffusion Pipeline")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be done without making changes")
    parser.add_argument("--limit", type=int, help="Limit number of folders to process")
    parser.add_argument("--config", default="render_config.json", help="Path to config file")
    parser.add_argument("--scan-paths", nargs="+", default=["Characters", "equipment"], 
                       help="Paths to scan for retry flags")
    
    args = parser.parse_args()
    
    pipeline = RenderPipeline(args.config)
    pipeline.run(args.scan_paths, args.dry_run, args.limit)


if __name__ == "__main__":
    main()