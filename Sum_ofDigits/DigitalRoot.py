numerk1 = 19
numerk2 = 429
numerk19 = input("Введите число: ")
print(numerk19)


def digital_root(n):
    temlnumS = "".join(f"{n}")
    temlnumu = list(temlnumS)
    newmas = list()
    i = 0
    while i < len(temlnumu):
        tempint = int(temlnumu[i])
        newmas.append(tempint)
        i += 1

    temnfff = sum(newmas)

    print(temnfff)
    print(type(temnfff))
    return temnfff


# digital_root(numerk1)
# print("#####")
# digital_root(numerk2)
# print("#####")
# temper = digital_root(numerk19)
temnum222 = 0
if digital_root(numerk19) % 2 == 0:
    print(True)
else:
    temnum222 = digital_root(numerk19) % 2
    print(False)
    print(temnum222)
