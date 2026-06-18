from abc import abstractmethod, ABC
from dataclasses import dataclass

@dataclass
class SmartDevice(ABC):
    name: str
    is_on: bool = False

    #@abstractmethod
    def toggle(self):
        if self.is_on: self.is_on = False
        else: self.is_on = True

    def __str__(self):
        return super().__str__()

    def __post_init__(self):
        if not self.name:
            raise ValueError("Device is not has name!")
    

my_lamp_1 = SmartDevice("lamp_1", False)

print(my_lamp_1)