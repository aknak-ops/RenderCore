# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

RenderCore is an AI-powered fitness exercise rendering system that generates images of the "Athia Fit" character performing various exercises. The system uses pose data, prompt engineering, and overlay generation to create fitness content.

## Key Architecture

### Core Components
- **render_single.py / render_batch.py**: Main rendering entry points that handle individual renders and batch processing
- **scripts/**: Contains rendering logic, utilities, and processing scripts  
- **core/**: Core system modules including backend processing and plugin architecture
- **render_batches/**: JSON batch configuration files defining exercise sets to render
- **renders/**: Output directory for generated exercise images and metadata

### Plugin System
The system appears to use a plugin-based architecture with:
- Plugin configuration in `core/backend/plugins.config`
- Plugin loading and routing capabilities
- Style and overlay plugins for customizing render output

### Configuration System
- **rendercore_config.json**: Main system configuration (active system, paths, logging)
- **render_settings.json**: Image quality and size settings
- **config.json**: Theme and output directory defaults
- **ai_pose_lookup.json**: Exercise-to-pose mapping data
- **quality_flags.json**: Quality control and flagging system

## Common Development Commands

### Rendering Operations
```bash
# Run all batch renders in queue
run_render_queue.bat

# Run specific batch file
python render_batch.py test_batch

# Run single exercise render  
python render_single.py [exercise_name]

# Generate theme previews
python pose_utils/theme_generator.py
```

### System Management
```bash
# Clean up old logs
cleanup_logs.bat

# Clean up output files
cleanup_output.bat

# Reset theme settings
reset_themes.bat

# Validate system integrity
validate_systems.bat

# Check render output quality
validate_renders.bat
```

### Development Utilities
```bash
# View render statistics
render_stats.bat

# Scan for overlay issues
scan_overlays.bat

# Clear quality flags
clear_flags.bat

# Rerun flagged renders
rerun_flagged.bat
```

## PowerShell Function System

The system heavily uses PowerShell functions defined in `RenderCore_Functions.ps1` (and numbered variants) that provide:
- Logging and session tracking
- Backup management before renders
- Batch processing workflows
- System state management

## Batch Processing Workflow

1. Define exercise batches in `render_batches/` as JSON files
2. Use `run_render_queue.bat` to process all batches
3. Monitor output in `renders/` directory
4. Review quality flags and reprocess if needed
5. Use validation tools to check render integrity

## File Organization

- **Top-level scripts**: Core rendering and utilities
- **commands/**: Wrapper batch files for common operations  
- **scripts/**: Large collection of utility and processing scripts
- **core/**: System core with backend processing
- **config/**: Configuration templates and settings
- **debug/**: Error logs and debugging information
- **logs/**: System operation logs and analytics

## Development Notes

- The system uses JSON-based configuration throughout
- Extensive PowerShell automation for Windows environment
- Quality control system with flagging and retry mechanisms
- Built-in backup and recovery systems
- Modular plugin architecture for extensibility