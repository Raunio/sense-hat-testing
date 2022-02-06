class SensorData:
    name = ""
    data = 0
    def __init__(self, name):
        self.name = name
    def set(self, data):
        self.data = data
    def toString(self):
        return self.name[0:1] + ": " + str(self.data)[0:4]