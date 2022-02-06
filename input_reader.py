class InputReader:
    def __init__(self, senseHat):
        self.senseHat = senseHat
    def read(self):
        while True:
            for event in self.senseHat.stick.get_events():
                print(event.direction, event.action)