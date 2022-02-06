from enum import Enum
class EventType(Enum):
    INPUT = 1,
    SENSOR_DATA = 2

class Event:
    def __init__(self, type: EventType, data, label):
        self.type = type
        self.data = data
        self.label = label
    def msg(self):
        return self.data