"""
class Epl:
    def work(self):
        print("working")


class Stud:
    def stud(self):
        print("stud")


class Complex(Epl, Stud):
    pass


tom = Complex()
tom.work()
tom.stud()
"""


class Employee:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def work(self):
        print(f"{self.name} works")


class Student:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def stidy(self):
        print(f"{self.name} studies")


class WokStud(Employee, Student):
    pass


ogi44 = WokStud("Gojira")
ogi44.work()
ogi44.stidy()
