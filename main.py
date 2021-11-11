import json
import requests
import time

dummyPayload = requests.get("https://painkillergis.com/1352x955.jpg").content

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
            requests.put(f"{baseURL}/{heightmap['id']}/heightmap.jpg", generate(heightmap))


def generate(heightmap):
    return dummyPayload


main()
