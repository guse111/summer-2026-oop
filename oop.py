from abc import abstractmethod, ABC

class Filament(ABC):
    def __init__(self, type, color, weight, temp):
        self.type = type
        self.color = color
        self.weight = weight
        self.temp = temp

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
        return f"Катушка {self.type} ({self.color}), осталось {self._weight}г"

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if value > 0:
            self._weight = value
        else:
            return None
        pass 
        

class PLA_Filament(Filament):
    def __init__(self, type, color, weight, temp, is_biodegradable):
        super().__init__(type, color, weight, temp)
        self.is_biodegradable = is_biodegradable
    def dry(self, hours):
        print(f"Сушим PLA {hours} часов при 45 градусах")

class Printer:
    def __init__(self):
        pass
    def print_model(self, filament, grams):
        if filament.use(grams):
            print("printing is started!")
        else: 
            None

    
#my_filament = Filament("PETG", "transparent", 1000, 230)
my_PLA = PLA_Filament("PLA", "grey", 1000, 215, True)

my_printer = Printer()

print(my_PLA)

