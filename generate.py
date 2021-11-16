import json
import os
import random
import sys


def generate(layout):
    with open('/tmp/junk', 'w') as f:
        f.write("junk junk junk " + str(random.randint(0, 1000)))
    return '/tmp/junk'


if __name__ == "__main__":
    hillshade = generate(json.load(sys.stdin))
    with open(hillshade, 'rb') as f:
        sys.stdout.buffer.write(f.read())
    os.remove(hillshade)
