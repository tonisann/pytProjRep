class Pers001:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def display_info(self):
        print(f"Name: {self.__name}")


class Empl001(Pers001):
    def __init__(self, name, company):
        super().__init__(name)
        self.company = company

    def display_info(self):
        super().display_info()
        print(f"Company: {self.company}")

    def work(self):
        print(f"{self.name} works")


tom88 = Empl001("Xert", "BERD")
tom88.display_info()

def act(person):
    if isinstance(person, Empl001):
        person.work()
    elif isinstance(person, Pers001):
        person.display_info()


act(tom88)
hoji = Pers001("gikurage")
act(hoji)