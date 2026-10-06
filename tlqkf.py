print("hi")

class Person:
    def __init__(self, name, age, point = 0):
        self.name = name
        self.age = age
        self.point = point
    def add_point(self, point):
        self.point += point
    def __str__(self):
        return f"Person(name={self.name}, age={self.age}, point={self.point})"

class TaxCalc:
    def calculate(self, price):
        return price * 0.1

class Pricelabel:
    def __init__(self, calc):
        self.calc = calc
    def text(self, price):
        t = self.calc.calculate(price)
        return f"Price: {price}, Tax: {t}"