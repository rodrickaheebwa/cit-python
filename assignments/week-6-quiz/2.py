# create Animal class and Dog class. Make the Dog class inherit from the Animal class. Add a bark method to the Dog class. Create an instance of the Dog class and call the bark method.

class Animal:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour

    def __str__(self):
        return f"Name : {self.name} \n Colour : {self.colour}"

class Dog(Animal):
    def __init__(self, name, colour):
        super().__init__(name, colour)

    def bark(self):
        print(f"Dog {self.name} says woof woof.")

    def __str__(self):
        return f"Dog Name : {self.name} \n Dog Colour : {self.colour}"

my_dog = Dog('Alex', 'brown')
my_dog.bark()