from abc import abstractmethod, ABC
from dataclasses import dataclass

class DeviceError(Exception):
    pass

@dataclass
class SmartDevice(ABC):
    name: str
    is_on: bool = False

    @abstractmethod
    def toggle(self):
        None
    def __str__(self):
        if self.is_on:
            return f"Устройство {self.name} включено"
        else: 
            return f"Устройство {self.name} выключено"
    def __post_init__(self):
        if not self.name:
            raise ValueError("Device is not has name!")
        
@dataclass
class SmartBulb(SmartDevice):
    brightness: int = 0
    def toggle(self):
        if self.is_on: 
            self.is_on = False
            self.brightness = 0
            print(f"Лампочка {self.name} погасла")
        else: 
            self.is_on = True
            self.brightness = 80
            print(f"Лампочка {self.name} загорелась с яркостью {self.brightness}%")
    def __post_init__(self):
        if self.brightness not in range(0,101):
            raise DeviceError( f"Яркость лампочки {self.name} вышла за пределы 0-100 ({self.brightness})")




my_lamp_1 = SmartBulb("lamp_1")

print(my_lamp_1)