#!/bin/bash
# Workspace backup script
# Runs git add, commit, push to backup workspace to GitHub

cd /home/openclaw/.openclaw/workspace

# Add all changes
git add -A

# Check if there are changes to commit
if git diff --staged --quiet; then
    echo "No changes to backup"
    exit 0
fi

# Commit with timestamp
TIMESTAMP=$(date "+%Y-%m-%d %H:%M")
git commit -m "Backup: $TIMESTAMP"

# Push to GitHub
git push origin main

echo "Backup complete: $TIMESTAMP"