# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

a = int(input('Первое число: '))
b = int(input('Второе число: '))

def calc(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        print(f'Ошибка! Делить на ноль нельзя')

print(calc(a, b))