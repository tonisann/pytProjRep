class Pytit:
    dofolt_name = "undef"
    type = "farina23"
    description = "bot model 001"

    def __init__(self, name):
        if name:
            self.name = name
        else:
            self.name = Pytit.dofolt_name

    def __str__(self):
        return f"Name: {self.name} Type: {self.type} Description: {self.description}"

    def dysp_info(self):
        print(f"Name: {self.name} Type: {self.type} Description: {self.description}")


print(Pytit.type)
print(Pytit.description)

Pytit.number = "1"
print(Pytit.number)

forge = Pytit("jotaro")
forge.dysp_info()


bertos = Pytit(Pytit.number)
bertos.dysp_info()
print(forge)
