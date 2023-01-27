import os
import time


def demo():
    print("1 - Демонстрация списка")
    print("2 - Добавление элемента в спискок")
    print("3 - Удаление элемента из списка")
    print("4 - Сортировка списка")
    print("5 - Выход")


spisok = []

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    time.sleep(1)
    demo()
    n = input("Введите число от 1 до 5...>")
    if n == '1':
        clear()
        print(spisok)
    elif n == '2':
        clear()
        print("Нажмите 1 чтобы внести элемент по индексу")
        print("Нажмите 2 чтобы внести элемент в конец списка")
        n = (input("Как будем добавлять?.....>"))
        if n == '1':
            clear()
            i = int(input("Введите индекс нового эелемента списка.....>"))
            item = input("Введите новый эелемент списка.....>")
            spisok.insert(i, item)
        elif n == '2':
            clear()
            print("Напишите элемент который неоходимо внести в конец списка....>")
            ch = input()
            spisok.append(ch)
        else:
            print("Введите правильное значение")
    elif n == '3':
        clear()
        i = int(input("Введите индекс удаляемого элемента списка.....>"))
        print(spisok)
        spisok.pop(i)
        print(f"{i}-й элемент списка удален")
        print("Новый список")
        print(spisok)
    elif n == '4':
        clear()
        print("Массив отсортирован")
        print(sorted(spisok))
    elif n == "5":
        break
    else:
        print("Введите правильное значение!!!")
