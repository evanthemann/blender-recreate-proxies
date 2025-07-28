import bpy

def do_proxy_rebuild():
    scene = bpy.context.scene
    if not scene.sequence_editor:
        print("No sequence editor found.")
        return None  # stop the timer

    areas = [area for area in bpy.context.window.screen.areas if area.type == 'SEQUENCE_EDITOR']
    if not areas:
        print("No SEQUENCE_EDITOR area open.")
        return None

    area = areas[0]
    region = next((r for r in area.regions if r.type == 'WINDOW'), None)

    with bpy.context.temp_override(window=bpy.context.window, area=area, region=region):
        for strip in scene.sequence_editor.sequences:
            if hasattr(strip, 'proxy'):
                strip.proxy.build_25 = True
                strip.proxy.build_50 = False
                strip.proxy.build_75 = False
                strip.proxy.build_100 = False
                strip.proxy.use_overwrite = True
                strip.select = True  # select all strips

        bpy.ops.sequencer.rebuild_proxy()
        print("✅ Proxies rebuilt for all strips at 25%.")

    return None  # stop repeating timer

# Run after Blender UI is ready
bpy.app.timers.register(do_proxy_rebuild, first_interval=1.0)

