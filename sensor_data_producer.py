import asyncio
from constants import Constants
from event import Event, EventType

class SensorDataProducer:
    def __init__(self, reader, label):
        self.reader = reader
        self.label = label
    async def read(self, queue):
        while True:
            await(queue.put(Event(EventType.SENSOR_DATA, self.reader(), self.label)))
            await asyncio.sleep(Constants.UPDATE_INTERVAL)
