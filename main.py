import json
import os

import asyncio
import sys

import requests

import websockets

from generate import generate

args = sys.argv[1:]
priority = args[0]

async def main():
    while True:
        try:
            await server(priority)
        except:
            print("restarting after exception")


async def server(priority):
    async with websockets.connect(f"wss://layouts.painkillergis.com/v1/awaiting_hillshade?priority={priority}") as ws:
        while True:
            await ws.send("")
            layout = json.loads(await ws.recv())
            hillshade = generate(layout)
            with open(hillshade, 'rb') as f:
                requests.put(f"https://layouts.painkillergis.com/v1/layouts/{layout['id']}/hillshade.jpg", f.read())
            os.remove(hillshade)
            await ws.send("")


asyncio.run(main())
