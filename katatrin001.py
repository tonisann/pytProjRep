def is_isogram(string):
    tempString = string.lower()
    # print(tempString)
    f1sp = list()
    f2sp = set()
    for char in tempString:
        f1sp.append(char)
        f2sp.add(char)
        # print(char)
    print(len(f1sp))
    print(len(f2sp))

    if len(f1sp) == len(f2sp):
        return True
    else:
        return False


userinput1 = input("Введите строку: ")
print(is_isogram(userinput1))


# is_isogram('kjaldkNDJASKDJ')
def fibonacci(n: int) -> int:
    return 0
