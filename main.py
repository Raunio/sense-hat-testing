import asyncio
from sense_hat import SenseHat
from sensor_data import SensorData
from sensor_reader import SensorReader
from time import sleep

updateInterval = 0.5
async def show(sense, sensor):
    sense.show_letter(str(sensor.data)[3])


loop = asyncio.get_event_loop()
try:
    sense = SenseHat()
    pressure = SensorData("Pressure")
    temp = SensorData("Temperature")

    readers = [ SensorReader(sense.get_pressure, pressure), SensorReader(sense.get_temperature, temp) ]

    current = temp

    for reader in readers:
        asyncio.ensure_future(reader.read())

    asyncio.ensure_future(show(sense, current))

    loop.run_forever()
except Exception as e:
    print(e)
    pass
finally:
    print("Closing Loop")
    loop.close()

def next_reader(current, readers):
    length = len(readers)
