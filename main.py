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
    response = requests.get(baseURL)
    heightmaps = response.json()

    for heightmap in heightmaps:
        if heightmap["imageURL"] == "":
            with open(generate(sourcePath, heightmap), 'rb') as f:
                requests.put(f"{baseURL}/{heightmap['id']}/heightmap.jpg", f.read())


main()
