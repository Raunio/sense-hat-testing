import asyncio
from event import Event, EventType
from constants import Constants


class StickInputProducer:
    def __init__(self, senseHat):
        self.senseHat = senseHat
    async def read(self, queue):
        while True:
            for event in self.senseHat.stick.get_events():
                if event.action == "pressed":
                    await queue.put(Event(EventType.INPUT, event.direction, Constants.LABEL_STICK_INPUT))

            await asyncio.sleep(Constants.INPUT_UPDATE_INTERVAL)