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