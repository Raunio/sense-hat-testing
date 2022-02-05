import asyncio

class SensorReader:
    updateInterval = 0.5
    def __init__(self, reader, out):
        self.reader = reader
        self.out = out
    async def read(self):
        while True:
            self.out.set(self.reader())
            await asyncio.sleep(self.updateInterval)
