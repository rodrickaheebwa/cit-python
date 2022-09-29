# Your task is to create slightly different animals, which should have the same properties and methods, but should implement the talk() method in different ways. For example. should a cat (when talking) say "Moew", a dog "Woff", a fish "Blub" and a Cow "Muuu". They should all share the following (private) properties: name (string), age (number), food (list of strings), and have the functions get_name, set_name, get_age, set_age, get_food, add_food, remove_food. Finally, all the animals must have the talk function, but that function must, as I said, be implemented in each animal, as the animals have different sounds.
# When you have made the classes, create instances of the classes and put in a list - loop through the list - and let all the animals talk! :)

class Animal:
    def __init__(self, name, age, food):
        self.__name = name
        self.__age = age
        self.__food = food

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        self.__name = new_age

    def get_food(self):
        return self.__food

    def add_food(self, food_item):
        self.__food.append(food_item)

    def remove_food(self, food_item):
        self.__food.remove(food_item)

class Cat(Animal):
    def __init__(self, name, age, food):
        super().__init__(name, age, food)

    def talk(self):
        return f"Cat {self.get_name()} says meow"

class Dog(Animal):
    def __init__(self, name, age, food):
        super().__init__(name, age, food)

    def talk(self):
        return f"Dog {self.get_name()} says woff"

class Cow(Animal):
    def __init__(self, name, age, food):
        super().__init__(name, age, food)

    def talk(self):
        return f"Cow {self.get_name()} says mooo"

class Fish(Animal):
    def __init__(self, name, age, food):
        super().__init__(name, age, food)

    def talk(self):
        return f"Fish {self.get_name()} says blub"

rodric = Cat('riko', 4, ['beans', 'posho'])
rodrik = Cow('riko', 4, ['beans', 'posho'])
rodick = Fish('riko', 4, ['beans', 'posho'])
rodrck = Dog('riko', 4, ['beans', 'posho'])

print(rodick.talk())
print(rodrck.talk())
print(rodric.talk())
print(rodrik.talk())