import random

mas_num = list(range(13, 101, 7))
# print(mas_num)
random.shuffle(mas_num)
# print(mas_num)
temp_num = random.choice(mas_num)
# print(temp_num)

numbers = list(range(1, 6))
print(numbers)


def find_average(numbers):
    print(numbers)
    temp111 = len(numbers)
    print(sum(numbers) / temp111)
    return sum(numbers) / temp111


find_average(numbers)

"""def count_sheeps(sheep):
    ct_se = 0
    for ct_se001 in sheep:
        if ct_se001 == True:
            ct_se += 1

    return ct_se"""

"""n = 10
mas_num001 = list(range(1, n + 1))
print(mas_num001)"""

"""def pre_fizz(n):
    mas_num001 = list(range(1, n + 1))
    return mas_num001"""

"""num_nmf001 = random.random() # *100
print(num_nmf001)"""

"""num_nmf002 = random.randint(13, 101)
print(num_nmf002)"""

"""num_nmf003 = random.randrange(1000, 10000, 1000)
print(num_nmf003)"""
