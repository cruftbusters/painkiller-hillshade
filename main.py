import os
import sys

import requests
import time

from generate import generate

args = sys.argv[1:]
sources = [
    {"minGroundSpacing": int(minGroundSpacing), "path": sourcePath}
    for minGroundSpacing, sourcePath in zip(args[::2], args[1::2])
]
baseURL = "https://gallery.painkillergis.com/v1/maps"


def main():
    while True:
        tick()
        time.sleep(2.5)


def tick():
    for metadata in requests.get(baseURL).json():
        if metadata["imageURL"] == "":
            heightmap = generate(sources, metadata)
            with open(heightmap, 'rb') as f:
                requests.put(f"{baseURL}/{metadata['id']}/heightmap.jpg", f.read())
            os.remove(heightmap)
            os.remove(f"{heightmap}.aux.xml")


main()
