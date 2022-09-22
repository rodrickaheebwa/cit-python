# create a class called Person. The class should have the following attributes: name, age, and address. The class should have the following methods: eat, sleep, and work. The eat method should print out the name of the person and the word "is eating". The sleep method should print out the name of the person and the word "is sleeping". The work method should print out the name of the person and the word "is working".

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def work(self):
        print(f"{self.name} is working.")