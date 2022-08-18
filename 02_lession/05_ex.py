# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

rating_el = int(input("Enter number: "))
my_list = [7, 4, 3, 2]
print(f"Current list:\n{my_list}")

c = my_list.count(rating_el)
for element in my_list:
    if c > 0:
        i = my_list.index(rating_el)
        my_list.insert(i+c, rating_el)
        break
    else:
        if rating_el > element:
            j = my_list.index(element)
            my_list.insert(j, rating_el)
            break
        elif rating_el < my_list[len(my_list) - 1]:
            my_list.append(rating_el)
print(f"Changed list:\n{my_list}")