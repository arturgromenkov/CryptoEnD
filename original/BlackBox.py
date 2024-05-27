from abc import ABC, abstractmethod
class BlackBox(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def predict(self, data):
        pass

