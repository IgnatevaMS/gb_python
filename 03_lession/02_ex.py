# Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.


def get_info(name, lastname, year_of_birth, city, email, phone):
    return print(f'Имя: {name} ,Фамилия: {lastname} ,Год рождения: {year_of_birth} '
                 f'Город проживания: {city} ,Email: {email} ,Телефон: {phone}')


get_info(
    name=input('Укажите имя>> '),
    lastname=input('Укажите фамилию>> '),
    year_of_birth=input('Укажите год рождения>> '),
    city=input('Укажите город проживания>> '),
    email=input('Укажите email>> '),
    phone=input('Укажите phone>> '),
)