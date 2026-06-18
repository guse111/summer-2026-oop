

class Filament:
    def __init__(self, type, color, weight, temp):
        self.type = type
        self.color = color
        self.weight = weight
        self.temp = temp
    
my_filament = Filament("PLA", "grey", 1000, 215)


print(my_filament.weight, my_filament.temp)
