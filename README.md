# Blender Recreate Proxies

Rebuilds sequence editor proxies at 25% resolution for all strips in a Blender project. Opens the `.blend` file in Blender, selects every strip that supports proxies, and triggers a proxy rebuild automatically.

## Usage

1. Run the shell script:

   ```
   bash run-rebuild-proxies.sh
   ```

2. When prompted, enter the full path to your `.blend` file.

Blender will open the file with its UI and execute the proxy rebuild after a short delay.

You can also run the Python script directly with Blender:

```
/Applications/Blender.app/Contents/MacOS/Blender /path/to/file.blend --python recreate-proxies.py
```

## Requirements

- macOS (the default Blender path assumes `/Applications/Blender.app`)
- Blender installed at `/Applications/Blender.app/Contents/MacOS/Blender` (edit `BLENDER_PATH` in the shell script if your installation differs)
- The `.blend` file must contain a sequence editor with strips
