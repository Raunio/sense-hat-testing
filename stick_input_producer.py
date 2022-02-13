import asyncio
from constants import Constants


class StickInputProducer:
    def __init__(self, senseHat):
        self.senseHat = senseHat
    async def read(self):
        for event in self.senseHat.stick.get_events():
            if event.action == "pressed":
                print(event.direction)

    def create_task(self):
        task = asyncio.create_task(self.read())
        return task