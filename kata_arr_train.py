def xo(s):
    counterX = 0
    counterO = 0
    arrchx = list()
    arrcho = list()
    # count = 0
    temps = s.lower()
    tempsmn = set()
    for temp1 in temps:
        tempsmn.add(temp1)

    print(tempsmn)

    countearru = 0
    arrU = list()
    for temphu in tempsmn:
        arrU.append(temphu)
        countearru += 1
        print(f"Write: {arrU}")

    # tempsmn.add(temps)
    # print(tempsmn)
    for temp in temps:
        if temp == 'x':
            arrchx.append(temp)
            print(arrchx)
            counterX += 1
        else:
            temp == 'o'
            arrcho.append(temp)
            print(arrcho)
            counterO += 1

    if len(arrchx) == len(arrcho):
        return True
    else:
        return False


print(xo('XoxxooOOsdffwe'))

"""def xo(s):
    temp_har = s
    count_temp_x = 0
    count_temp_o = 0
    counter = 0
    for char in temp_har:
        if char == "x":
            count_temp_x += 1
            print(count_temp_x)
        elif char == "o":
            count_temp_o += 1
            print(count_temp_o)
        else:
            counter += 1
            print(counter)

    if count_temp_x == count_temp_o:
        return True
    else:
        return False"""


# xo('xo')
# print("next")
# xo('xo0')
# print("next")
# xo('xxxoo')


def check(seq, elem):
    for tepm in seq:
        if tepm == elem:
            return True

    return False


# https://www.codewars.com/kata/57cc975ed542d3148f00015b/train/python
def descending_order(num):
    x = num
    # x = 1234

    result = []
    while x > 0:
        result.append(x % 10)
        x //= 10

    result.reverse()
    result.sort()
    result.reverse()
    num1 = 0
    for i, v in enumerate(reversed(result)):
        num1 += v * 10 ** i
    return num1


"""x = 1234

result = []
while x > 0:
    result.append(x % 10)
    x //= 10

result.reverse()
print(result)  # [1, 2, 3, 4]

num1 = 0
for i, v in enumerate(reversed(result)):
    num1 += v * 10 ** i
print(num1)  # 1234"""
# descending_order(152)
# print(descending_order(562))
# temp1 = list(range(10))
# descending_order(temp1)
# print(temp1)
# number = 15
# result = []
# while number > 0
# arnum = list()
# arnum.append(number)
# arnum.sort()
# print(arnum)
# https://ru.stackoverflow.com/questions/749118/%D0%BF%D1%80%D0%B5%D0%BE%D0%B1%D1%80%D0%B0%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D1%87%D0%B8%D1%81%D0%BB%D0%B0-%D0%B2-%D1%81%D0%BF%D0%B8%D1%81%D0%BE%D0%BA
# https://www.codewars.com/kata/5467e4d82edf8bbf40000155/train/python
