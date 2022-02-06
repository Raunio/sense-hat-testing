import asyncio
from globals import Globals
class SensorReader:
    def __init__(self, reader):
        self.reader = reader
    async def read(self, queue):
        while True:
            await(queue.put(self.reader()))
            await asyncio.sleep(Globals.UPDATE_INTERVAL)
