import asyncio
from constants import Constants
from mqtt_connection_provider import MQTTConnectionProvider
from sensor_data import SensorData

class SensorDataProducer:
    def __init__(self, mqtt_connection: MQTTConnectionProvider):
        self.mqtt_connection = mqtt_connection

    def reader(self, reader):
        self.reader = reader
        return self

    def tag(self, tag):
        self.tag = tag
        return self

    def unit(self, unit):
        self.unit = unit
        return self

    async def read(self):
        while True:
            self.mqtt_connection.publish("rasp/sensehat", SensorData().name(self.tag).unit(self.unit).data(self.reader()).toJSON())
            await asyncio.sleep(Constants.UPDATE_INTERVAL)

    def create_task(self):
        task = asyncio.create_task(self.read())
        return task