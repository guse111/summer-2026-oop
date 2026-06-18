from abc import abstractmethod, ABC
from dataclasses import dataclass, field

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
    brightness: int = 80
    def toggle(self):
        if self.is_on: 
            self.is_on = False
            print(f"Лампочка {self.name} погасла")
        else: 
            self.is_on = True
            print(f"Лампочка {self.name} загорелась с яркостью {self.brightness}%")
    def __post_init__(self):
        super().__post_init__()
        if self.brightness not in range(0,101):
            raise DeviceError( f"Яркость лампочки {self.name} вышла за пределы 0-100 ({self.brightness})")

@dataclass
class SmartSocket(SmartDevice):
    max_power: float = 20
    def toggle(self):
        if self.is_on: 
            self.is_on = False
            print(f"Розетка {self.name} выключена")
        else: 
            self.is_on = True
            print(f"Розетка {self.name} подает напряжение. Лимит: {self.max_power} Вт")

my_lamp_1 = SmartBulb("lamp_1")
my_soket_1 = SmartSocket("soket_1", False, 50)
my_soket_2 = SmartSocket("soket_2", False, 50)


@dataclass
class SmartHome():
    devices: list = field(default_factory=list)
    def add_device(self, device: SmartDevice):
        self.devices.append(device)

    def status(self):
        for device in self.devices:
            print(device)
    def turn_all_off(self):
        for device in self.devices:
            if device.is_on:
                device.toggle()

my_home = SmartHome()

try:
    bad_lamp = SmartBulb("bad", brightness=150)
except DeviceError as e:
    print(f"Ошибка: {e}")

my_home.add_device(my_lamp_1)
my_home.add_device(my_soket_1)
my_home.status()
my_home.turn_all_off()