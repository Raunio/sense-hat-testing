class SensorData:
    name = ""
    data = 0
    def __init__(self, name):
        self.name = name
    def set(self, data):
        print(data)
        self.data = data
    def toString(self):
        return self.name + ": " + str(self.data)