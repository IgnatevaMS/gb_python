# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме
# и после этого завершить программу.

def calc_numbers():
    res = 0
    while True:
        numbers = input('Введите список чисел через пробел или * для выхода: ').split()
        for i in numbers:
            try:
                if i == '*':
                    print(f'Сумма чисел: {res}. Выход')
                    return
                else:
                    res += int(i)
            except ValueError:
                print('Введите число или * для выхода')
        print(f'Сумма чисел: {res}')

calc_numbers()