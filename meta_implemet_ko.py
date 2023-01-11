class Pers001:

    def __init__(self, name001):
        self.__name = name001

    @property
    def name(self):
        return self.__name

    def display_info(self):
        print(f"Name: {self.__name}")


class Employee001:

    def __init__(self, name001):
        self.__name = name001

    @property
    def name(self):
        return self.__name

    def display_info(self):
        print(f"name: {self.__name}")

    def work(self):
        print(f"{self.name} works")


class Employee002(Pers001):

    def work(self):
        print(f"{self.name} work")


tom001 = Employee002("Tommigan")
print(tom001.name)
tom001.display_info()
tom001.work()
