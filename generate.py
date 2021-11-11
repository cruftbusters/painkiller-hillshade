import json
import sys

import requests

dummyPayload = requests.get("https://painkillergis.com/1352x955.jpg").content


def generate(metadata):
    return dummyPayload


if __name__ == "__main__":
    sys.stdout.buffer.write(generate(json.load(sys.stdin)))
