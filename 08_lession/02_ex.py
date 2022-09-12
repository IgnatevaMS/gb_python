# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class LocalError(Exception):
    def __init__(self, txt):
        self.txt = txt


def checker():
    try:
        num_1 = int(input('Введите делимое: '))
        num_2 = int(input('Введите делитель: '))
        if num_2 == 0:
            raise LocalError("Делить на ноль нельзя!")
        else:
            result = num_1 / num_2
            return result
    except ValueError:
        return "Введено не число"
    except LocalError as err:
        return err

print(checker())
