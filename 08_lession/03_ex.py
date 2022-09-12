# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере.
# Необходимо запрашивать у пользователя данные и заполнять список только числами.
# Класс-исключение должен контролировать типы данных элементов списка.

class MyError(Exception):
    def __init__(self):
        pass


class TypeCheck:
    def __init__(self):
        self.user_list = []

    def check_input_value(self):
        global user_val
        while True:
            try:
                try:
                    user_val = int(input('Введите число: '))
                    ex = input(f'Число "{user_val}" добавлено в список. Продолжить? y/n: ').lower()
                    self.user_list.append(user_val)
                    if ex == 'n':
                        print('Сформирован список:')
                        print(self.user_list)
                        break
                except ValueError:
                    raise MyError
            except MyError:
                ex = input(f"Введено не число! Продолжить? y/n: ").lower()
                if ex == 'n':
                    print('Сформирован список:')
                    print(self.user_list)
                    break
                else:
                    self.check_input_value()


a = TypeCheck()
a.check_input_value()