#!/usr/bin/env python3
"""
Script to concatenate all chapters into a single master document.
Reads all chapter files from the 'chapters' directory and outputs them to stdout.
Optionally converts straight quotes to curly quotes using the smartypants library.
"""

import argparse
import os
import sys
from pathlib import Path

# Optional dependency on smartypants for smart quote conversion
try:
    import smartypants
    SMARTYPANTS_AVAILABLE = True
except ImportError:
    SMARTYPANTS_AVAILABLE = False

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Concatenate all chapters into a single master document."
    )
    parser.add_argument(
        "-s", "--smart-quotes",
        action="store_true",
        help="Convert straight quotes to curly quotes using smartypants"
    )
    parser.add_argument(
        "-d", "--chapters-dir",
        default="chapters",
        help="Directory containing chapter files (default: chapters)"
    )
    return parser.parse_args()

def main():
    # Parse command line arguments
    args = parse_arguments()
    
    # Check if smart quotes requested but smartypants not available
    if args.smart_quotes and not SMARTYPANTS_AVAILABLE:
        print("Error: smartypants library is required for smart quote conversion.", file=sys.stderr)
        print("Install it with: pip install smartypants", file=sys.stderr)
        sys.exit(1)
    
    # Get the script's directory and find the chapters directory
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    chapters_dir = project_root / args.chapters_dir
    
    if not chapters_dir.exists():
        print(f"Error: Chapters directory not found at {chapters_dir}", file=sys.stderr)
        sys.exit(1)
    
    # Get all markdown files in the chapters directory
    chapter_files = []
    for file_path in chapters_dir.glob("*.md"):
        chapter_files.append(file_path)
    
    # Sort files by name to ensure correct order (01_, 02_, etc.)
    chapter_files.sort(key=lambda x: x.name)
    
    if not chapter_files:
        print("Error: No chapter files found in chapters directory", file=sys.stderr)
        sys.exit(1)
    
    # Concatenate all chapters
    for i, chapter_file in enumerate(chapter_files):
        try:
            with open(chapter_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
                # Apply smart quote conversion if requested
                if args.smart_quotes:
                    content = smartypants.smartypants(content)
                
                # Add the content to stdout
                print(content, end='')
                
                # Add a separator between chapters (except for the last one)
                if i < len(chapter_files) - 1:
                    print("\n\n")
                    
        except Exception as e:
            print(f"Error reading {chapter_file}: {e}", file=sys.stderr)
            sys.exit(1)

if __name__ == "__main__":
    main()
