import requests

dummyPayload = requests.get("https://painkillergis.com/1352x955.jpg").content


def generate(heightmap):
    return dummyPayload
