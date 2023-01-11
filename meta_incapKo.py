class Pers001:
    def __init__(self, name001):
        self.name001 = name001
        self.age001 = 1

    def disp_inf(self):
        print(f"your name: {self.name001} your age: {self.age001}")


tom001 = Pers001("Obj_001")
tom001.name001 = "human name"
tom001.age001 = -113
tom001.disp_inf()


class Pers002:
    def __init__(self, name002):
        self.__name = name002  # переменная доступна только в нутри класса
        self.__age = 1

    def set_age(self, age):
        if 1 < age < 110:
            self.__age = age
        else:
            print("Недоступный возраст")

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name

    def disp_info(self):
        print(f"Имя: {self.__name}\tВозраст: {self.__age}")


tom002 = Pers002("Ferdis")
tom002.disp_info()
tom002.set_age(33)
tom002.disp_info()


class Pers003:
    def __init__(self, name):
        self.__name = name
        self.__age = 1

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if 1 < age < 110:
            self.__age = age
        else:
            print("Недоступный возраст")

    @property
    def name(self):
        return self.__name

    def disp_info(self):
        print(f"Имя: {self.__name} \t Возраст: {self.__age}")


tom003 = Pers003("ObjKL003")

tom003.disp_info()
tom003.age = -555
print(tom003.age)
tom003.age = 44
tom003.disp_info()
