from abc import abstractmethod, ABC
from dataclasses import dataclass
from random import randint

@dataclass
class Character(ABC):
    name: str
    hp: int
    max_hp: int
    damage: int
    defense: int

    def take_damage(self, amount):
        damage = max(0, amount - self.defense)  # Урон не может быть отрицательным
        self.hp -= damage
    
    def is_alive(self):
        return self.hp > 0
    
    def attack(self, target):
        target.take_damage(self.damage)

    @abstractmethod
    def special_attack(self, target):
        pass

@dataclass
class Warrior(Character):

    def special_attack(self, target):
        target.take_damage(randint(int(self.damage), self.damage*2))
        #добавить оглушение


@dataclass
class Mage(Character):
    mana: int
    max_mana: int
    mana_regen: int = 0
    
    def __post_init__(self):
        self.mana_regen = int(self.max_mana * 0.2)

    def mana_consumption(self, mana):
        self.mana -= mana

    def mana_regeneration(self):
        regen = self.mana_regen + int(self.mana * 0.1)
        self.mana = min(self.max_mana, self.mana + regen) 


    def special_attack(self, target):
        target.take_damage(randint(self.damage*3, self.damage*4))
        self.mana_consumption(int(self.max_mana*0.5))

    def mana_attack(self, target):

        damage = randint(int(self.damage*1.2), self.damage*2)
        if self.mana > damage:
            target.take_damage(damage)
            self.mana_consumption(damage)
        else:
            print('"Среньк", маны оказалось маловато.')

@dataclass
class Archer(Character):
    arrows: int = 5

    def arrow_consumption(self, arrows = 1):
            self.arrows -= arrows

    def special_attack(self, target):
        target.take_damage(self.damage*2)
    
    def shot(self, target):
        if self.arrows>0:
            target.take_damage(int(self.damage*1.3))
            self.arrow_consumption()
        else:
            print('"Пук", стрел не хватило.')


# Создаём персонажей
warrior = Warrior("Конан", 100, 100, 15, 5)
mage = Mage("Гэндальф", 50, 50, 10, 3, 100, 100)
archer = Archer("Леголас", 60, 60, 12, 3, 20)

# Создаём врага
goblin = Warrior("Гоблин", 40, 40, 8, 2)

# Тест атак
print(f"Гоблин HP до: {goblin.hp}")
warrior.attack(goblin)
print(f"После атаки воина: {goblin.hp}")

mage.mana_attack(goblin)
print(f"После магической атаки: {goblin.hp}")

archer.shot(goblin)
print(f"После выстрела лучника: {goblin.hp}")
print(f"Стрел осталось: {archer.arrows}")

# Тест регенерации маны
print(f"\nМана мага до: {mage.mana}")
mage.mana_regeneration()
print(f"После регенерации: {mage.mana}")
    