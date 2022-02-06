class SensorReader:
    def __init__(self, reader, out):
        self.reader = reader
        self.out = out
    def read(self):
        self.out.set(self.reader())
        print(self.out.data)
