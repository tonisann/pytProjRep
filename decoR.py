# определение функции декоратора
def select(input_func):
    def output_func():  # определяем функцию, которая будет выполняться вместо оригинальной
        print("*****************")  # перед выводом оригинальной функции выводим всякую звездочки
        input_func()  # вызов оригинальной функции
        print("*****************")  # после вывода оригинальной функции выводим всякую звездочки

    return output_func  # возвращаем новую функцию


# определение оригинальной функции
@select  # применение декоратора select
def hello():
    print("Hello METANIT.COM")


# вызов оригинальной функции
hello()