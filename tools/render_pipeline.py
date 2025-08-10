#!/usr/bin/env python3
"""
RenderCore Stable Diffusion Pipeline
Scans for retry_flag.txt files and generates missing PNG phases using AUTOMATIC1111 API.
"""

import os
import sys
import json
import time
import base64
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
    def __init__(self, config_path: str = "render_config.json", verbose: bool = False, cli_overrides: Optional[Dict] = None):
        self.config = self.load_config(config_path)
        self.verbose = verbose
        self.cli_overrides = cli_overrides or {}
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
            "default_phases": 3,
            "payload": {
                "steps": 20,
                "width": 512,
                "height": 512,
                "cfg_scale": 7,
                "sampler_name": "Euler a",
                "negative_prompt": ""
            }
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

    def log_message(self, message: str, print_also: bool = True, verbose_only: bool = False):
        """Write message to log file and optionally print."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {message}\n"
        
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(log_entry)
        
        if print_also and (not verbose_only or self.verbose):
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
        
        self.log_message(f"Checking {num_phases} phases in {folder.name}: {len(missing_phases)} missing", 
                        verbose_only=True)
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
            with open(prompt_file, 'r', encoding='utf-8-sig') as f:
                prompt = f.read().strip()
                # Remove any remaining BOM characters
                prompt = prompt.lstrip('\ufeff')
                return prompt
        except Exception as e:
            self.log_message(f"ERROR: Could not read prompt from {prompt_file}: {e}")
            return None

    def preflight_check(self, dry_run: bool = False) -> bool:
        """Check if AUTOMATIC1111 API is accessible."""
        if dry_run:
            return True
            
        try:
            url = f"{self.config['base_url']}/sdapi/v1/progress"
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                self.log_message(f"✓ AUTOMATIC1111 API accessible at {self.config['base_url']}")
                return True
            else:
                print(f"ERROR: AUTOMATIC1111 API returned status {response.status_code}")
                return False
        except Exception:
            print(f"ERROR: Cannot connect to AUTOMATIC1111 at {self.config['base_url']}")
            print(f"Solution: Start webui-user.bat with --api flag")
            print(f"Example: set COMMANDLINE_ARGS=--api --xformers --listen")
            print(f"Current base_url: {self.config['base_url']}")
            return False

    def call_automatic1111_api(self, prompt: str) -> Optional[bytes]:
        """Call AUTOMATIC1111 txt2img API and return image bytes."""
        url = f"{self.config['base_url']}/sdapi/v1/txt2img"
        
        # Use configurable payload from config, with CLI overrides
        payload = self.config['payload'].copy()
        payload['prompt'] = prompt
        
        # Apply CLI overrides
        if 'steps' in self.cli_overrides:
            payload['steps'] = self.cli_overrides['steps']
        if 'cfg_scale' in self.cli_overrides:
            payload['cfg_scale'] = self.cli_overrides['cfg_scale']
        if 'sampler_name' in self.cli_overrides:
            payload['sampler_name'] = self.cli_overrides['sampler_name']
        
        self.log_message(f"API Call: {url[:50]}... with prompt: {prompt[:30]}...", verbose_only=True)
        
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
                        image_data = base64.b64decode(result['images'][0])
                        self.log_message(f"SUCCESS: Generated image ({len(image_data)} bytes)", verbose_only=True)
                        return image_data
                    else:
                        self.log_message(f"ERROR: No images in API response")
                        return None
                else:
                    error_text = response.text[:200] if response.text else "No error details"
                    self.log_message(f"ERROR: API returned status {response.status_code}: {error_text}")
                    
            except requests.exceptions.Timeout:
                self.log_message(f"WARNING: API timeout on attempt {attempt + 1}/{self.config['retries']}")
            except requests.exceptions.ConnectionError:
                self.log_message(f"WARNING: Connection error on attempt {attempt + 1}/{self.config['retries']} - Is AUTOMATIC1111 running?")
            except Exception as e:
                self.log_message(f"ERROR: API call failed: {e}")
            
            if attempt < self.config['retries'] - 1:
                backoff_time = self.config['backoff_sec'] * (attempt + 1)
                self.log_message(f"Retrying in {backoff_time} seconds...", verbose_only=True)
                time.sleep(backoff_time)
        
        self.log_message(f"ERROR: All {self.config['retries']} attempts failed for prompt: {prompt[:50]}...")
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
            self.log_message(f"ERROR: Cannot process {folder} - no valid prompt.txt")
            return False
        
        # Check what phases are missing (use CLI override if provided)
        num_phases = self.cli_overrides.get('phases', self.config['default_phases'])
        missing_phases = self.get_missing_phases(folder, num_phases)
        
        if not missing_phases:
            num_phases = self.cli_overrides.get('phases', self.config['default_phases'])
            self.log_message(f"SKIP: All {num_phases} phases exist in {folder.name}")
            self.stats["skipped"] += 1
            return True
        
        self.log_message(f"Missing phases: {missing_phases} (prompt: {prompt[:60]}...)")
        
        if dry_run:
            self.log_message(f"DRY-RUN: Would generate {len(missing_phases)} images")
            return True
        
        # Generate missing images
        success = True
        generated_count = 0
        
        for phase_filename in missing_phases:
            final_filename = self.get_versioned_filename(folder, phase_filename)
            self.log_message(f"Generating: {final_filename}")
            
            image_data = self.call_automatic1111_api(prompt)
            if image_data:
                file_path = folder / final_filename
                if self.save_image(image_data, file_path):
                    self.log_message(f"SUCCESS: Saved {final_filename} ({len(image_data)} bytes)")
                    self.stats["images_generated"] += 1
                    generated_count += 1
                else:
                    success = False
                    self.stats["errors"] += 1
                    self.log_message(f"ERROR: Failed to save {final_filename}")
            else:
                self.log_message(f"ERROR: Failed to generate image for {phase_filename} - API call failed")
                success = False
                self.stats["errors"] += 1
        
        if success and generated_count > 0:
            self.log_message(f"Folder complete: Generated {generated_count}/{len(missing_phases)} images")
        elif not success:
            self.log_message(f"Folder failed: Generated {generated_count}/{len(missing_phases)} images")
        
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
        mode = "DRY-RUN" if dry_run else "PRODUCTION"
        
        # Preflight check
        if not self.preflight_check(dry_run):
            if not dry_run:
                sys.exit(1)
            else:
                self.log_message("DRY-RUN: Skipping API connectivity check")
        
        self.log_message(f"=== RenderCore Pipeline Started ({mode}) ===")
        phases = self.cli_overrides.get('phases', self.config['default_phases'])
        self.log_message(f"Config: {self.config['base_url']}, timeout={self.config['timeout_sec']}s, phases={phases}")
        if self.cli_overrides:
            self.log_message(f"CLI Overrides: {self.cli_overrides}")
        self.log_message(f"Scan paths: {scan_paths}")
        if limit:
            self.log_message(f"Limit: {limit} folders")
        
        # Find folders with retry flags
        retry_folders = self.find_retry_folders(scan_paths)
        self.log_message(f"Found {len(retry_folders)} folders with retry flags")
        
        if len(retry_folders) == 0:
            self.log_message("No folders found. To trigger renders, create 'retry_flag.txt' in exercise folders.")
            return
        
        if limit:
            retry_folders = retry_folders[:limit]
            self.log_message(f"Limited to first {limit} folders")
        
        # Process each folder
        for i, folder in enumerate(retry_folders, 1):
            self.log_message(f"--- Processing {i}/{len(retry_folders)}: {folder.name} ---")
            
            success = self.process_folder(folder, dry_run)
            self.stats["folders_processed"] += 1
            
            if success and not dry_run:
                self.remove_retry_flag(folder)
            elif not success:
                self.log_message(f"FAILED: Leaving retry flag in {folder.name} for retry")
        
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
        
        if self.stats['errors'] > 0:
            print(f"\nSome folders had errors. Check {self.log_file} for details.")
            print(f"Retry flags were left in failed folders for re-processing.")
        elif self.stats['images_generated'] > 0:
            print(f"\nPipeline completed successfully!")
        elif self.stats['skipped'] > 0:
            print(f"\nAll target images already exist (skipped folders).")


def main():
    parser = argparse.ArgumentParser(
        description="RenderCore Stable Diffusion Pipeline",
        epilog="Example: python tools/render_pipeline.py --dry-run --limit 3 --phases 4 --steps 30"
    )
    parser.add_argument("--dry-run", action="store_true", 
                       help="Show what would be done without making changes")
    parser.add_argument("--limit", type=int, 
                       help="Limit number of folders to process")
    parser.add_argument("--verbose", "-v", action="store_true", 
                       help="Enable verbose logging output")
    parser.add_argument("--config", default="render_config.json", 
                       help="Path to config file (default: render_config.json)")
    parser.add_argument("--scan-paths", nargs="+", default=["Characters", "equipment"], 
                       help="Paths to scan for retry flags (default: Characters equipment)")
    
    # CLI overrides for generation parameters
    parser.add_argument("--phases", type=int, 
                       help="Override number of phases to generate")
    parser.add_argument("--steps", type=int, 
                       help="Override number of diffusion steps")
    parser.add_argument("--cfg", type=float, 
                       help="Override CFG scale value")
    parser.add_argument("--sampler", type=str, 
                       help="Override sampler name (e.g., 'Euler a', 'DPM++ 2M Karras')")
    
    args = parser.parse_args()
    
    # Build CLI overrides dict
    cli_overrides = {}
    if args.phases is not None:
        cli_overrides['phases'] = args.phases
    if args.steps is not None:
        cli_overrides['steps'] = args.steps
    if args.cfg is not None:
        cli_overrides['cfg_scale'] = args.cfg
    if args.sampler is not None:
        cli_overrides['sampler_name'] = args.sampler
    
    # Print startup info
    if args.verbose or args.dry_run:
        print(f"RenderCore Pipeline - {'DRY RUN' if args.dry_run else 'PRODUCTION'}")
        print(f"Config: {args.config}")
        print(f"Scan paths: {args.scan_paths}")
        if args.limit:
            print(f"Limit: {args.limit}")
        if cli_overrides:
            print(f"CLI Overrides: {cli_overrides}")
        print()
    
    pipeline = RenderPipeline(args.config, args.verbose, cli_overrides)
    pipeline.run(args.scan_paths, args.dry_run, args.limit)


if __name__ == "__main__":
    main()