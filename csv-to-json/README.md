# CSV to JSON Converter

A simple command‑line utility that converts a CSV file into a JSON file.

## Features
- Takes an input CSV file and an output JSON file path via command‑line arguments.
- Optional `--pretty` flag to produce indented (human‑readable) JSON.
- Basic error handling for missing files and malformed CSV.

## Usage
```bash
python convert.py input.csv output.json [--pretty]
```

- `input.csv` – Path to the source CSV file (must contain a header row).
- `output.json` – Desired path for the resulting JSON file.
- `--pretty` – If provided, the JSON will be formatted with indentation.

## Example
```bash
python convert.py data/users.csv data/users.json --pretty
```

## Requirements
The script uses only Python's standard library (no external packages), so there are no additional dependencies.
