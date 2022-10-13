# create a class called Vehicle. The class should have the following attributes: make, model, and year. The class should have the following methods: start, stop, and drive. The start method should print out the make, model, and year of the vehicle and the word "is starting". The stop method should print out the make, model, and year of the vehicle and the word "is stopping". The drive method should print out the make, model, and year of the vehicle and the word "is driving". Create a subclass of Vehicle called Car. The Car class should have the following attributes: make, model, year, and color. The Car class should have the following methods: start, stop, drive, and park. The park method should print out the make, model, year, and color of the car and the word "is parking". Create an instance of the Car class and call all the methods.

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print(f"The {self.make} {self.model} {self.year} is starting.")

    def stop(self):
        print(f"The {self.make} {self.model} {self.year} is stopping.")

    def drive(self):
        print(f"The {self.make} {self.model} {self.year} is driving.")

class Car(Vehicle):
    def __init__(self, make, model, year, color):
        self.color = color
        super().__init__(make, model, year)

    def park(self):
        print(f"The {self.make} {self.model} {self.year} is parking.")

m = Car('Ford', 'ranger', 2020, 'black')
m.start()
m.drive()
m.stop()
m.park()