from original.BlackBox import BlackBox

class MemeBox(BlackBox):
    def __init__(self):
        super().__init__()

    def predict(self, data):
        print(data)

box = MemeBox()

