import os
import sys

import requests
import time

from generate import generate


def main():
    while True:
        tick("https://layouts.painkillergis.com")
        time.sleep(2.5)


def tick(baseURL):
    try:
        response = requests.get(f"{baseURL}/v1/layouts?withHeightmapWithoutHillshade=true")
        if response.status_code == 200:
            for layout in response.json():
                hillshade = generate(layout)
                with open(hillshade, 'rb') as f:
                    requests.put(f"{baseURL}/v1/layouts/{layout['id']}/hillshade.jpg", f.read())
                os.remove(hillshade)
        else:
            print(
                "Failed to communicate with layout service",
                f"got status code: {response.status_code}",
                file=sys.stderr,
            )
    except requests.exceptions.RequestException as e:
        print("Failed to communicate with layout service", e, file=sys.stderr)


main()
