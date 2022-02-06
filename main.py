import asyncio
from sense_hat import SenseHat
from globals import Globals
from sensor_data import SensorData
from sensor_reader import SensorReader
from time import sleep
from repeatable_task import RepeatableTask
from input_reader import InputReader

async def show(sense, selectedData):
    sense.show_letter(selectedData.name[0])

loop = asyncio.get_event_loop()
try:
    senseHat = SenseHat()
    pressure = SensorData("Pressure")
    temp = SensorData("Temperature")

    readers = [ SensorReader(senseHat.get_pressure, pressure), SensorReader(senseHat.get_temperature, temp) ]

    selectedData = temp
    
    for reader in readers:
        repeatable = RepeatableTask(reader.read, True)
        loop.create_task(repeatable.update())

    #loop.create_task(show(senseHat, selectedData))
    inputReader = InputReader(senseHat)
    loop.create_task(asyncio.to_thread(inputReader.read))
    #await inputTask

    loop.run_forever()
except Exception as e:
    print(e)
    pass
finally:
    print("Closing Loop")
    loop.close()
    senseHat.clear()

def next_reader(current, readers):
    length = len(readers)