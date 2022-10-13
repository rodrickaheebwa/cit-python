# create a class of your choice. It should have at least 3 attributes and 3 methods where one of the methods is a static method. Implement polymorphism, encapsulation, and inheritance.

class UniversityPersonnel():
    def __init__(self, name, age, school):
        self.__name = name
        self.__age = age
        self.school = school

    def greet():
        print("Hello!")

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


class Professor(UniversityPersonnel):
    def __init__(self, name, age, school, department):
        self.department = department
        super().__init__(name, age, school)

    def status(self):
        print(f"{self.get_name()} is a professor at the school of {self.school} under the department of {self.department}")

    def teach(self):
        print(f"{self.get_name()} is teaching.")


class Student(UniversityPersonnel):
    def __init__(self, name, age, school, course):
        self.course = course
        super().__init__(name, age, school)

    def greet():
        print("Hello!")

    def study(self):
        print(f"{self.get_name()} is studying.")

    def status(self):
        print(f"{self.get_name()} is a student at the school of {self.school} pursuing a degree in {self.course}")

student = Student('rodrick', 22, 'computing', 'computer science')
professor = Professor('Allan', 58, 'computing', 'networks')

UniversityPersonnel.greet()
student.study()
student.status()

professor.teach()
professor.status()