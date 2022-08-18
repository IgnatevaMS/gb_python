# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

month = int(input("Please enter month id from 1 to 12 : "))
if month <= 12 and month >= 1:
    # Решение через справочник
    seasons = {1: "зима", 2: "весна", 3: "лето", 4: "осень"}
    months_dict = {1: seasons.get(1), 2: seasons.get(1), 3: seasons.get(2), 4: seasons.get(2), 5: seasons.get(2),
                   6: seasons.get(3), 7: seasons.get(3), 8: seasons.get(3), 9: seasons.get(4), 10: seasons.get(4),
                   11: seasons.get(4), 12: seasons.get(1)}
    value = months_dict[month] if month in months_dict else print(f"Your month id {month} is not found in seasons")
    print(f"\tSearch result in seasons dictionary for month id# {month} is:  '{value}'")

    # Решение через List
    mlist = ["зима", "весна", "лето", "осень"]
    mlist = ["зима", "весна", "лето", "осень"]
    if month == 12 or (month >= 1 and month < 3):
        print(f"\tSeason related to your Month id#{month}  is '{mlist[0]}'")
    elif month >= 3 and month < 6:
        print(f"\tSeason related to your Month id# {month} is '{mlist[1]}'")
    elif month >= 6 and month < 9:
        print(f"\tSeason related to your Month id# {month} is '{mlist[2]}'")
    elif month >= 9 and month < 12:
        print(f"\tSeason related to your Month id# {month} is '{mlist[3]}'")

else:
    print("You made a mistake.Incorrect month number")
