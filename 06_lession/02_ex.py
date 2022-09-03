# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна.
# Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т

class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weight = 25
        self.height = 5

    def asphalt_mass(self):
        asphalt_mass = self._length * self._width * self.weight * self.height / 1000
        print(f'длина: {round(self._length)}')
        print(f'ширина: {round(self._width)}')
        print(f'масса: {round(self.weight)}')
        print(f'толщина: {round(self.height)}')

        print (f'Рассчет: {round(self._length)}*{round(self._width)}*{round(self.weight)}*{round(self.height)}/1000')

        print(f'Ответ: Для покрытия всего дорожного полотна неободимо {round(asphalt_mass)} массы асфальта')


r = Road(5000, 20)
r.asphalt_mass()