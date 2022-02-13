import json
from unicodedata import name


class SensorData:
    def name(self, name):
        self.name = name
        return self
    def data(self, data):
        self.data = data
        return self
    def unit(self, unit):
        self.unit = unit
        return self
        
    def toJSON(self):
        return json.dumps({ "tag": self.name, "value": self.data, "unit": self.unit })