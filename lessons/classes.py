# a class has properties and behaviour, attributes and methods
# def __init__ function initialises instance attributes
# class attributes are defined outside the __init__ and are the same for all instances of a class

import string
import random

class Employee:
    def __init__(self, name, salary, age, department):
        self.salary = salary
        self.name = name
        self.age = age
        self.department = department
        self.id = self.create_employee_ID()


    def create_employee_ID(self):
        emp_id = "EMP"
        for _ in range(2):
            emp_id += random.choice(string.ascii_letters)
        for _ in range(3):
            emp_id += random.choice(string.digits)
        return emp_id

    def __repr__(self):
        return f"Name: {self.name} \n Salary: {self.salary} \n Age: {self.age} \
         \n Department: {self.department} \n ID: {self.id}"

class Animal:
    def __init__(self):
        self.name = "cow"
        self.color = "Brown"

    def change_name(self, name):
        self.name = name

    def print_animal(self):
        print(f"{self.name} {self.color}")


cow = Animal()
print(cow.name)
cow.change_name("Some Cow")
print(cow.name)
cow.print_animal()

class Car:
    def __init__(self, model, color, brand, price):
        self.model = model
        self.color = color
        self.brand = brand
        self.price = price

    def move(self, direction, speed):
        print(f"{self.brand} is moving in {direction} direction at a speed of {speed} km/h")

    def stop(self):
        print(f"{self.brand} has stopped")

    def update_price(self, price):
        self.price = price
        print(f"The new price is {self.price}")