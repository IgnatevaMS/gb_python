# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

from datetime import date

class Data:
    def __init__(self, data):
        self.data = data.split('-')

    @classmethod
    def type(cls, data):
        try:
            day, month, year = [int(i) for i in data.split('-')]
            return f'Корректно: {data}'
        except ValueError:
            return f'Указана неправильная дата1:{data}'

    @staticmethod
    def valid(data):
        try:
            day, month, year = data.split('-')
            date(int(year), int(month), int(day))
            return f'Корректно: {data}'
        except ValueError:
            return f'Указана неправильная дата2: {data}'


print(Data.valid('25-02-2015'))
print(Data.valid('25-13-2015'))
print(Data.type('25-02'))
print(Data.type('01-01-2020'))

