import json, requests, time


def main():
    while True:
        tick()
        time.sleep(2.5)


def tick():
    response = requests.get("https://gallery.painkillergis.com/v1/maps")
    heightmaps = response.json()

    for heightmap in heightmaps:
        if heightmap["imageURL"] == "":
            process(heightmap)


def process(heightmap):
    requests.patch(
        f"https://gallery.painkillergis.com/v1/maps/{heightmap['id']}",
        json.dumps({"imageURL": "https://painkillergis.com/1352x955.jpg"}),
    )


main()
