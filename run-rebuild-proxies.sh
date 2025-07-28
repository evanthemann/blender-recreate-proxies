#!/bin/bash

# Ask for the .blend file
read -rp "Enter the full path to the .blend file: " blend_file

# Expand any escape characters (for drag-and-drop)
blend_file=$(eval echo "$blend_file")

# Check if file exists
if [ ! -f "$blend_file" ]; then
  echo "❌ .blend file does not exist: $blend_file"
  exit 1
fi

# Blender path (update if needed)
BLENDER_PATH="/Applications/Blender.app/Contents/MacOS/Blender"

# Run Blender, open the blend, and run the Python script (keeping UI open)
"$BLENDER_PATH" "$blend_file" --python recreate-proxies.py

