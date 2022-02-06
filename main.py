import asyncio
from sense_hat import SenseHat
from sensor_data import SensorData
from sensor_reader import SensorReader
from input_reader import InputReader
from conditional import Conditional

class Main:
    senseHat = SenseHat()

    async def printConsumer(self, queue):
        while True:
            msg = await queue.get()
            print(msg)
            queue.task_done()

    async def main(self):
        try:
            queue = asyncio.Queue()
            inputReader = InputReader(self.senseHat)
            pressureReader = SensorReader(self.senseHat.get_pressure)
            tempReader = SensorReader(self.senseHat.get_temperature)
            producers = [ asyncio.create_task(pressureReader.read(queue)), asyncio.create_task(inputReader.read(queue)), asyncio.create_task(tempReader.read(queue)) ]
            consumers =  [ asyncio.create_task(self.printConsumer(queue)) ]

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
            print("Closing Loop")
            self.loop.close()
            self.senseHat.clear()
            

main = Main()
asyncio.run(main.main())