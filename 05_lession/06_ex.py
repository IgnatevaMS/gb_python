# Необходимо создать (не программно) текстовый файл,
# где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий
# по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.


if __name__ == "__main__":
    lession = {}

    try:
        with open('test6.txt', encoding='utf-8') as fh:
            lines = fh.readlines()

        for line in lines:
            data = line.replace('(', ' ').split()

            lession[data[0][:-1]] = sum(
                int(i) for i in data if i.isdigit()
            )
    except IOError as e:
        print(e)
    except ValueError:
        print("Некорректные данные")
    print("Словарь:")
    print(lession)
