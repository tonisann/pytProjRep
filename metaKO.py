class Person01:  # инициализация класса
    pass  # указывает что клас без параметров и методов


tom01 = Person01()  # создается обьект класса


class Person02:
    def say_hello(self):  # первый параметр self - ссылка на текущий обьект (метод класса)
        print("Hi Yujin!")


tom02 = Person02()
tom02.say_hello()


class Person03:
    def say(self, message):  # если есть параметры, то они указываются после self
        print(message)


tom03 = Person03()
tom03.say("how are you?")


class Person04:
    def say04(self, message):
        print(message)

    def say_hello04(self):
        self.say04("rojer wiljam")


tom04 = Person04()
tom04.say_hello04()


class Person05:
    def __init__(self):
        print("Create object P05")

    def say_hello05(self):
        print("Hi P05")


tom05 = Person05()
tom05.say_hello05()


class Person06:
    def __init__(self, name):
        self.name = name  # this
        self.age = 1  #


tom06 = Person06("Tom")

print(tom06.name)
print(tom06.age)

tom06.age = 37

print(tom06.age)


class Person07:
    def __init__(self, name):
        self.name = name
        self.age = 1


tom07 = Person07("P07")

tom07.compani = "SCBCVNNQ"
print(tom07.compani)


class Person08:
    def __init__(self, name):
        self.name = name
        self.age = 1

    def display_info(self):
        print(f"Name: {self.name} Age: {self.age}")


tom08 = Person08("Honjo")
tom08.display_info()


class Person09:
    def __init__(self, name):
        self.name = name
        self.age = 1

    def display_info(self):
        print(f"Name: {self.name} Age: {self.age}")


tom09 = Person09("Rojer")
tom09.age = 26
tom09.display_info()

job09 = Person09("Folter")
job09.age = 28
job09.display_info()
