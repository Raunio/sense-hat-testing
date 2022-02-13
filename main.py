import asyncio
from cProfile import label
import sys
import traceback
from sense_hat import SenseHat
from mqtt_connection_provider import MQTTConnectionProvider
from sensor_data_producer import SensorDataProducer
from stick_input_producer import StickInputProducer
from constants import Constants

async def main():
    senseHat = SenseHat()
    mqttConnectionProvider = MQTTConnectionProvider()

    try:
        inputProducer = StickInputProducer(senseHat)

        pressureProducer = SensorDataProducer(mqttConnectionProvider)
        pressureProducer.reader(senseHat.get_pressure)
        pressureProducer.tag(Constants.TAG_PRESSURE)
        pressureProducer.unit(Constants.UNIT_PRESSURE)

        tempProducer = SensorDataProducer(mqttConnectionProvider)
        tempProducer.reader(senseHat.get_temperature)
        tempProducer.tag(Constants.TAG_TEMPERATURE)
        tempProducer.unit(Constants.UNIT_TEMPERATURE)

        humidityProducer = SensorDataProducer(mqttConnectionProvider)
        humidityProducer.reader(senseHat.get_humidity)
        humidityProducer.tag(Constants.TAG_HUMIDITY)
        humidityProducer.unit(Constants.UNIT_HUMIDITY)

        compassProducer = SensorDataProducer(mqttConnectionProvider)
        compassProducer.reader(senseHat.get_compass)
        compassProducer.tag(Constants.TAG_COMPASS)
        compassProducer.unit(Constants.UNIT_COMPASS)

        orientationProducer = SensorDataProducer(mqttConnectionProvider)
        orientationProducer.reader(senseHat.get_orientation)
        orientationProducer.tag(Constants.TAG_ORIENTATION)
        orientationProducer.unit("dunno")

        producers = [ 
            #pressureProducer.create_task(), 
            #inputProducer.create_task(), 
            #tempProducer.create_task(), 
            #humidityProducer.create_task(),
            #compassProducer.create_task() 
            orientationProducer.create_task() ]

        await asyncio.gather(*producers)

    except Exception as e:
        print(e)
        traceback.print_exception(*sys.exc_info())
        pass
    finally:
        senseHat.clear()
        mqttConnectionProvider.cleanup()
            
if __name__ == "__main__":
    asyncio.run(main())