# Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
#   сложение (add()),
#   вычитание (sub()),
#   умножение (mul()),
#   деление (truediv()).
# Данные методы должны применяться только к клеткам и выполнять увеличение,
# уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно

class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return f'Результат операции: {self.quantity * "*"}'

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):

        return self.quantity - other.quantity if (self.quantity - other.quantity) > 0 else print('Отрицательно!')


    def __mul__(self, other):
        return Cell(int(self.quantity * other.quantity))

    def __truediv__(self, other):
        return Cell(round(self.quantity // other.quantity))


    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.quantity / cells_in_row)):
            row += f'{"*" * cells_in_row} \\n'
        row += f'{"*" * (self.quantity % cells_in_row)}'
        return row

cells1 = Cell(33)
cells2 = Cell(9)
print(f'Ячейка: {cells1}')

print(f'Сложение: {(cells1 + cells2)}')

print(f'Вычитание: {(cells2 - cells1)}')

print(f'Деление: {(cells1 / cells2)}')

print(f'Ряд1: {cells2.make_order(5)}')
print(f'Ряд2: {cells1.make_order(10)}')

