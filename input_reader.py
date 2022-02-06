import asyncio

from globals import Globals


class InputReader:
    def __init__(self, senseHat):
        self.senseHat = senseHat
    async def read(self, queue):
        while True:
            for event in self.senseHat.stick.get_events():
                if event.action == "pressed":
                    await queue.put(event.direction)

            await asyncio.sleep(Globals.INPUT_UPDATE_INTERVAL)