import asyncio
from cProfile import label
from sense_hat import SenseHat
from event import EventType
from sensor_data import SensorData
from sensor_data_producer import SensorDataProducer
from stick_input_producer import StickInputProducer
from constants import Constants

class Main:
    senseHat = SenseHat()

    async def inputEventConsumer(self, queue):
        while True:
            event = await queue.get()
            if(event.type == EventType.INPUT):
                print(event.msg())
            if(event.type == EventType.SENSOR_DATA and event.label == Constants.LABEL_TEMPERATURE):
                if(event.data > 25):
                    print("Its getting hot in here! Temp is ", event.data)

            queue.task_done()

    async def main(self):
        try:
            queue = asyncio.Queue()

            inputProducer = StickInputProducer(self.senseHat)
            pressureProducer = SensorDataProducer(self.senseHat.get_pressure, Constants.LABEL_PRESSURE)
            tempProducer = SensorDataProducer(self.senseHat.get_temperature, Constants.LABEL_TEMPERATURE)

            producers = [ asyncio.create_task(pressureProducer.read(queue)), asyncio.create_task(inputProducer.read(queue)), asyncio.create_task(tempProducer.read(queue)) ]
            consumers =  [ asyncio.create_task(self.inputEventConsumer(queue)) ]

            # with both producers and consumers running, wait for
            # the producers to finish
            await asyncio.gather(*producers)
            print('---- done producing')
        
            # wait for the remaining tasks to be processed
            await queue.join()
        
            # cancel the consumers, which are now idle
            for c in consumers:
                c.cancel()
        except Exception as e:
            print(e)
            pass
        finally:
            self.senseHat.clear()
            

main = Main()
asyncio.run(main.main())