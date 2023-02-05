spisok = '1 3 5 7 9 11 13 15 2 4 6 8 10 12 14 16 18 20 '
at = [int(x) for x in spisok.split()]

try:
    user = int(input("Введите целое число от 1 до 20: "))
    if user % 1 == 0:
        at.append(user)
        print("Список до сортировки: ", at)
        at.sort()
        print("Список после сортировки по возрастанию: ", at)
    else:
        print("введите корректное число")
except ValueError:
    print("Не корректные данные.")
    print("Программа завершена!")
