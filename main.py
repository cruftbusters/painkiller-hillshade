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
            process(heightmap)


def process(heightmap):
    mapURL = f"{baseURL}/{heightmap['id']}"
    heightmapURL = f"{mapURL}/heightmap.jpg"
    requests.put(heightmapURL, dummyPayload)
    requests.patch(
        mapURL,
        json.dumps({"imageURL": heightmapURL}),
    )


main()
