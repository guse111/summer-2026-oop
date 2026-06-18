from abc import abstractmethod, ABC
from dataclasses import dataclass

@dataclass
class Filament(ABC):

    type: str
    color: str
    weight: int
    temp: int

    @abstractmethod
    def dry(self, hours):
        pass
    
    def check_amount(self, required_grams):
        return self.weight >= required_grams
    def use(self, grams):
        if self.check_amount(grams):
            self.weight -= grams
            return True
        else:
            print(f"Not enough filament")
            return False
    def __str__(self):
        return f"Катушка {self.type} ({self.color}), осталось {self.weight}г"
    
    
    def __post_init__(self):
        if self.weight < 0:
            raise ValueError("Вес не может быть отрицательным!")
     

class PLA_Filament(Filament):
    def __init__(self, type, color, weight, temp, is_biodegradable):
        super().__init__(type, color, weight, temp)
        self.is_biodegradable = is_biodegradable
    def dry(self, hours):
        print(f"Сушим PLA {hours} часов при 45 градусах")

@dataclass
class Nozzle:
    diameter: float
    material: str

@dataclass
class Printer:
    name: str
    nozzle: Nozzle
    def print_model(self, filament, grams):
        if filament.use(grams):
            print("printing is started!")
        else: 
            None
    def __str__(self):
        return f"Принтер {self.name} с соплом {self.nozzle.diameter} ({self.nozzle.material})"

    

my_PLA = PLA_Filament("PLA", "grey", 1000, 215, True)
my_nozzle = Nozzle(0.4, "brass")
my_printer = Printer("kobra S1", my_nozzle)
print(my_printer)


