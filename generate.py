import json
import os
import random
import requests
import subprocess
import sys
import tempfile


def generate(layout):
    response = requests.get(layout["heightmapURL"])
    heightmap = tempfile.mktemp()
    with open(heightmap, 'wb') as f:
        f.write(response.content)
    hillshade = tempfile.mktemp(suffix="#.jpg")
    width = layout['size']['width']
    height = layout['size']['height']
    scale = layout['scale']
    process = subprocess.run(["sh", "-c", f"blender -b -P blender.py -noaudio -o //{hillshade} -f 0 -- {heightmap} {width} {height} {scale}"], capture_output=True)
    os.remove(heightmap)
    if process.returncode != 0:
        print(process.stdout, file=sys.stderr)
    return hillshade.replace('#', '0')


if __name__ == "__main__":
    hillshade = generate(json.load(sys.stdin))
    with open(hillshade, 'rb') as f:
        sys.stdout.buffer.write(f.read())
    os.remove(hillshade)
