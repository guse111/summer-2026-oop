from random import randint
from dataclasses import dataclass
import numpy as np
import re

#2
#Задание: Определить класс-строку. Два конструктора: из строки символов и копированием. Предусмотреть функции слияния двух строк и подсчёта предложений в строке.
#help("str".count)


@dataclass
class String:
    string: str

    def copy(self):
        return String(self.string)

    def merge(self, other):
        return String(f"{self.string}{other.string}")

    def count_sentences(self):
        return len(re.findall(r'[.!?]+', self.string))
    


my_string = String("Hello ")
my_string2 = String("World....")
my_string3 = my_string.copy()
my_string.string = "Goodbye "
print(my_string.string)
print(my_string3.merge(my_string2).string)
print(my_string2.count_sentences())























#9
#Задание: Определить класс квадратной матрицы. Два конструктора: по размеру (со случайными числами) и копированием. Предусмотреть функции вычисления детерминанта и умножения матрицы на чис
#np.info(np.linalg.matmul)
#help(np)


"""
class Matrix:
    def __init__(self, size):
        self.data = np.random.randint(1, 20, size=(size, size))
    
    def copy_matrix(self):
        new_vector = Matrix(0)
        new_vector.data = self.data.copy()
        return new_vector
    
    def det(self):
        return round(np.linalg.det(self.data), 2)
    
    def mul(self, num):
        new_matrix = Matrix(0)
        new_matrix.data = self.data * num
        return new_matrix
    
my_matrix1 = Matrix(3)
my_matrix2 = my_matrix1.copy_matrix()

print(my_matrix1.data)
print(my_matrix1.det())
print(my_matrix2.mul(4).data)
"""
#11
#Задание: Определить класс вектор. Включить два конструктора: по размеру (со случайными числами) и копированием другого вектора. Предусмотреть функции умножения векторов и подсчёта суммы элементов.
"""
class Vector():
    def __init__(self, size):
        self.data = []
        for i in range(size):
            self.data.append(randint(-5, 5))
    
    def copy_vector(self):
        new_vector = Vector(0)
        new_vector.data = self.data.copy()
        return new_vector
    
    def multiplication(self, vector):
        if (len(self.data) != len(vector.data)):
            print("Длины векторов не совпадают!")
            return Vector(0)
        new_vector = Vector(0)
        for i in range(len(vector.data)):
            new_vector.data.append(self.data[i] * vector.data[i])
        return new_vector

    def sum_vector(self):
        return sum(self.data)
    
my_vector = Vector(5)
print(my_vector.data)
my_vector2 = Vector(6)
my_vector3 = my_vector.copy_vector()
print(my_vector.multiplication(my_vector2).data)
print(my_vector.multiplication(my_vector3).data)
print(my_vector.multiplication(my_vector3).sum_vector())
"""

#8
"""
class Labalist():
    def __init__(self, size):
        self.data = []
        for i in range(size):
            self.data.append(randint(1, 10))
    
    def list_copy(self):
        copy_list = Labalist(0)
        copy_list.data = self.data.copy()
        return copy_list
    
    def difference(self, other_list):
        new_list = Labalist(0)
        for i in self.data:
            if i not in other_list.data:
                new_list.data.append(i)
            
        for j in other_list.data:
            if j not in self.data:
                new_list.data.append(j)


        return new_list
    
    
    def sum_of_elements(self):
        return sum(self.data)


my_list = Labalist(10)
my_list2 = Labalist(10)
#copy_my_list = my_list.list_copy()
#print(copy_my_list.data)
print((my_list.data))
print((my_list2.data))
print(my_list.difference(my_list2).data)

#print(my_list.difference(my_list2).sum_of_elements())
# """