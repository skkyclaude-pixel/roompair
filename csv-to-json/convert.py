#!/usr/bin/env python3
"""csv-to-json converter

Usage:
    python convert.py input.csv output.json [--pretty]

- input.csv  : path to source CSV (must have a header row)
- output.json: path to write JSON output
- --pretty   : optional flag to pretty‑print JSON with indentation
"""

import argparse
import csv
import json
import sys
import os

def parse_args():
    parser = argparse.ArgumentParser(description="Convert a CSV file (with a header row) to a JSON array of objects.")
    parser.add_argument("input", help="Path to the input CSV file")
    parser.add_argument("output", help="Path to the output JSON file")
    parser.add_argument("--pretty", action="store_true", help="Pretty‑print JSON with 4‑space indentation")
    return parser.parse_args()

def read_csv(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Input CSV file not found: {path}")
    with open(path, newline="", encoding="utf-8") as f:
        try:
            reader = csv.DictReader(f)
            # Ensure there is a header row
            if reader.fieldnames is None:
                raise ValueError("CSV file appears to have no header row")
            rows = list(reader)
            return rows
        except csv.Error as e:
            raise ValueError(f"Error parsing CSV: {e}")

def write_json(data, path, pretty=False):
    try:
        with open(path, "w", encoding="utf-8") as f:
            if pretty:
                json.dump(data, f, indent=4, ensure_ascii=False)
            else:
                json.dump(data, f, separators=(",", ":"), ensure_ascii=False)
    except OSError as e:
        raise OSError(f"Failed to write JSON file: {e}")

def main():
    args = parse_args()
    try:
        rows = read_csv(args.input)
        write_json(rows, args.output, pretty=args.pretty)
        print(f"Successfully converted {len(rows)} rows to JSON: {args.output}")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
