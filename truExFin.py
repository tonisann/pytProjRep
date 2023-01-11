class Pers001:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def dispInf(self):
        print(f"Name: {self.__name} Age: {self.__age}")

    def __str__(self):
        return f"Name: {self.__name} Age: {self.__age}"


tomi = Pers001("Tombosino", 25)
tomi.dispInf()
print(tomi)
