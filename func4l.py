def outer():  # внешняя функция
    n = 5

    def inner():  # вложенная функция
        nonlocal n  # указываем, что n - это переменная из окружающей функции
        n = 25
        print(n)

    inner()  # 25
    print(n)


outer()  # 25


def multiply(n):
    def inner(m): return n * m

    return inner


print("next step")
fn = multiply(3)
print(fn(5))  # 25
print(fn(6))  # 30
print(fn(7))  # 35

#ljambda
def multiply(n): return lambda m: n * m

print("***")
fn = multiply(5)
print(fn(5))  # 25
print(fn(6))  # 30
print(fn(7))  # 35