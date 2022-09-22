# create a class called Employee. The class should have the following attributes: name, age, and salary. The class should have the following methods: eat, sleep, and work. The eat method should print out the name of the person and the word "is eating". The sleep method should print out the name of the person and the word "is sleeping". The work method should print out the name of the person and the word "is working". Create a subclass of Employee called Programmer. The Programmer class should have the following attributes: name, age, salary, and programming language. The Programmer class should have the following methods: eat, sleep, work, and code. The code method should print out the name of the person and the word "is coding in" and the programming language. Create an instance of the Programmer class and call all the methods.

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def work(self):
        print(f"{self.name} is working.")

class Programmer(Employee):
    def __init__(self, name, age, salary, programming_language):
        self.programming_language = programming_language
        super().__init__(name, age, salary)

    def code(self):
        print(f"{self.name} is coding in {self.programming_language}")

me = Programmer('rodrick', 22, 2000000, 'python')
me.eat()
me.sleep()
me.work()
me.code()