import json
import os

import asyncio
import requests

import websockets

from generate import generate


async def main():
    async with websockets.connect("wss://layouts.painkillergis.com/v1/awaiting_hillshade") as ws:
        while True:
            await ws.send("")
            layout = json.loads(await ws.recv())
            hillshade = generate(layout)
            with open(hillshade, 'rb') as f:
                requests.put(f"https://layouts.painkillergis.com/v1/layouts/{layout['id']}/hillshade.jpg", f.read())
            os.remove(hillshade)
            await ws.send("")


asyncio.run(main())
