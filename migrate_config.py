#!/usr/bin/env python3
"""
Migration script: Convert PyBLOCK config files from pickle to JSON format.

This script finds all .conf files used by PyBLOCK, reads them as pickle,
and rewrites them as JSON. A backup of each original file is created
with a .pickle.bak extension.

Usage:
    python3 migrate_config.py [directory]

If no directory is specified, it searches the current directory and
common PyBLOCK config locations.
"""

import json
import os
import pickle
import shutil
import sys


def find_conf_files(search_dirs):
    """Find all .conf files in the given directories."""
    conf_files = []
    for search_dir in search_dirs:
        if not os.path.isdir(search_dir):
            continue
        for root, _, files in os.walk(search_dir):
            for f in files:
                if f.endswith('.conf'):
                    conf_files.append(os.path.join(root, f))
    return conf_files


def is_pickle_file(filepath):
    """Check if a file is in pickle format (not valid JSON)."""
    try:
        with open(filepath, 'r') as f:
            json.load(f)
        return False  # Already JSON
    except (json.JSONDecodeError, UnicodeDecodeError, ValueError):
        try:
            with open(filepath, 'rb') as f:
                pickle.load(f)
            return True  # Valid pickle
        except Exception:
            return False  # Neither pickle nor JSON


def migrate_file(filepath):
    """Migrate a single .conf file from pickle to JSON."""
    if not is_pickle_file(filepath):
        return False, "already JSON or not a valid pickle file"

    try:
        # Read pickle data
        with open(filepath, 'rb') as f:
            data = pickle.load(f)

        # Create backup
        backup_path = filepath + '.pickle.bak'
        shutil.copy2(filepath, backup_path)

        # Write as JSON
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2, default=str)

        return True, f"migrated (backup: {backup_path})"

    except Exception as e:
        return False, f"error: {e}"


def main():
    if len(sys.argv) > 1:
        search_dirs = [sys.argv[1]]
    else:
        # Search common PyBLOCK config locations
        search_dirs = [
            '.',
            'config',
            'pybitblock',
            'pybitblock/config',
            'pybitblock/SPV',
            'pybitblock/SPV/config',
        ]

    conf_files = find_conf_files(search_dirs)

    if not conf_files:
        print("No .conf files found.")
        return

    print(f"Found {len(conf_files)} config file(s):\n")

    migrated = 0
    skipped = 0
    errors = 0

    for filepath in sorted(conf_files):
        success, message = migrate_file(filepath)
        status = "OK" if success else "SKIP"
        if "error" in message:
            status = "ERR"
            errors += 1
        elif success:
            migrated += 1
        else:
            skipped += 1

        print(f"  [{status}] {filepath} - {message}")

    print(f"\nResults: {migrated} migrated, {skipped} skipped, {errors} errors")


if __name__ == '__main__':
    main()
