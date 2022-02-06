class RepeatableTaskCondition:
    def __init__(self, val):
        self.val = val
    
    def fulfilled(self):
        return self.val == True