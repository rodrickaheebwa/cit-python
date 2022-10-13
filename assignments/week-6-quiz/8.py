# create a class called Animal. The class should have the following attributes: name, color, and age. The class should have the following methods: eat, sleep, and make_sound. The eat method should print out the name of the animal and the word "is eating". The sleep method should print out the name of the animal and the word "is sleeping". The make_sound method should print out the name of the animal and the word "is making a sound". Create a subclass of Animal called Dog. The Dog class should have the following attributes: name, color, age, and breed. The Dog class should have the following methods: eat, sleep, make_sound, and bark. The bark method should print out the name of the dog and the word "is barking". Create an instance of the Dog class and call all the methods.

class Animal:
    def __init__(self, name, colour, age):
        self.name = name
        self.colour = colour
        self.age = age

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def make_sound(self):
        print(f"{self.name} is making a sound.")

class Dog(Animal):
    def __init__(self, name, colour, age, breed):
        self.breed = breed
        super().__init__(name, colour, age)

    def bark(self):
        print(f"{self.name} is barking.")

my_dog = Dog('Alex', 'brown', 5, 'shiba inu')
my_dog.eat()
my_dog.sleep()
my_dog.make_sound()
my_dog.bark()