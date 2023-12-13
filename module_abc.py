from abc import ABC, abstractmethod
import math

# moduł abc do zdefiniowania abstrakcyjnej klasy bazowej o nazwie Shape, dodaj metodę abstrakcyjną o nazwie area
class Shape (ABC):
    @abstractmethod
    def area (self):
        pass

# Stwórz konkretną klasę dziedziczącą po klasie abstrakcyjnej Shape o nazwie Circle i dodaj funkcję obliczającą pole koła

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (self.radius ** 2) * round(math.pi,2)
    
# w metodzie __init__ klasy Rectangle ustaw wartość atrybutów width oraz height, w tej klasie zaimplementuj także metodę area liczącą pole prostokąta.
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height