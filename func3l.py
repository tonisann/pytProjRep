def print_person(name, age):
    if age > 120 or age < 1:
        print("Invalid age")
        return
    print(f"Name: {name} Age: {age}")


print_person("Tom", 22)
print_person("Bob", 150)
