def print_hello(mes):
    match mes:
        case "russian":
            print("Привет")
        case "english":
            print("Hello")
        case "german":
            print("Hallo")
        case _:
            print("Undefined")


print_hello("english1")  # Hello
print_hello("german1")  # Hallo
print_hello("russian1")  # Привет
