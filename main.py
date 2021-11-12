import sys

import requests
import time

from generate import generate


sourcePath = sys.argv[1]
baseURL = "https://gallery.painkillergis.com/v1/maps"


def main():
    while True:
        tick()
        time.sleep(2.5)


def tick():
    for metadata in requests.get(baseURL).json():
        if metadata["imageURL"] == "":
            with open(generate(sourcePath, metadata), 'rb') as f:
                requests.put(f"{baseURL}/{metadata['id']}/heightmap.jpg", f.read())


main()
