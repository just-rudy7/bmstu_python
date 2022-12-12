# Серышева ИУ7-14Б
#
# Требуется написать программу, которая позволит с помощью меню выполнить
# следующие действия по обработке базы данных, хранящейся в бинарном файле:
# + 1. Выбрать файл для работы
# + 2. Инициализировать базу данных
# + 3. Вывести содержимое базы данных
# + 4. Добавить запись в базу данных
# 5. Удалить запись из базы данных (по номеру в файле)
# + 6. Поиск по одному полю
# + 7. Поиск по двум полям

from struct import *


def deleting(file, form_len): # удаление
    f = open(file, 'rb+')
    f.seek(0, 2)
    size = f.tell()
    f.seek(0)
    num = None
    while num is None or not ((size // form_len) >= num > 0):
        try:
            num = int(input("Введите номер записи для удаления[1, {0}] :> ".format(size // form_len)))
        except ValueError:
            print("Ой, номер - число. Посторите ввод")
    
    num -= 1
    f.seek(0, 2)
    
    curr_num = num * form_len
    while curr_num + form_len < size:
        f.seek(curr_num + form_len)
        tmp = f.read(form_len)
        f.seek(curr_num)
        f.write(tmp)
        curr_num += form_len
    
    f.truncate(size - form_len)
    f.close()


def print_menu():  # вывод меню
    print("Список команд для работы с текстовыми базами данных:",
          "0 -> выход из программы", "1 -> выбрать файл для работы", "2 -> инициализация бд",
          "3 -> вывод содержимого бд", "4 -> добавить запись в конец бд", "5 -> удалить запись из бд (по номеру)",
          "6 -> поиск по одному полю в бд",
          "7 -> поиск по двум полям бд", "8 -> повторный вывод меню", sep="\n")


def output_bd(file, form, form_len): # вывод бд
    print("|{0:<10}|{1:^25}|{2:^25}|{3:^20}|".format('N', 'Кличка', "Порода", "Возраст (n лет)"))
    print("+", "-" * 83, "+", sep='')
    f = open(file, 'rb')
    f.seek(0, 2)
    size = f.tell()
    f.seek(0)
    for i in range(size // form_len):
        s_info = f.read(form_len)
        s_info = list(unpack(form, s_info))
        for j in range(3):
            # print(s_info[j])
            s_info[j] = s_info[j].decode('utf-8', errors='ignore')
            s_info[j] = s_info[j].replace('\x00', '')
            # print(s_info[j])
        print("|{0:<10}|{1:^25}|{2:^25}|{3:^20}|".format(i + 1, s_info[0], s_info[1], str(int(s_info[2]))))
    
    print()


def inn(str): # ввод строк
    s = input(str + " :> ")
    while len(s) > 25:
        print("Длина не больше 25 символов. Повторите ввод")
        s = input(str + " :> ")
    return s


def inn_age(str): # проверка возраста на число и величину
    s = input(str + " :> ")
    while not (len(s) <= 2 and s.isdecimal()):
        print("Длина не больше 2 символов и возраст - это число. Повторите ввод")
        s = input(str + " :> ")
    if len(s) == 1:
        s = "0" + s
    return s


def innit_db(file, form): # иннициализация
    n = int(input("Введите количество строк, которые хотите добавить: "))
    f = open(file, 'wb')
    for i in range(n):
        print("Введите данные о собаке: кличка, порода(строчными буквами) и возраст")
        name = inn("Кличка")
        breed = inn("Порода(строчными)")
        age = inn_age("возраст(количество полных лет [0;99])")
        s = pack(form, name.encode('utf-8'), breed.encode('utf-8'), age.encode('utf-8'))
        f.write(s)
    f.close()


def add_info(file, form, num):
    print()

# def add_info(file, form):
#     print("Введите данные о собаке: кличка, порода и возраст (не больше 25 сим)")
#     name = inn("Кличка")
#     breed = inn("Порода(строчными)")
#     age = inn_age("возраст(количество полных лет [0;99])")
#     s = pack(form, name.encode('utf-8'), breed.encode('utf-8'), age.encode('utf-8'))
#     # print(s)
#     # print(s)
#     f = open(file, 'ab')
#     f.write(s)
#     f.close()


def look_for_one(file, field, bred, form_len, form): # Поиск по одному полю
    flag = True
    f = open(file, 'rb')
    f.seek(0, 2)
    size = f.tell()
    f.seek(0)
    for i in range(size // form_len):
        s_info = f.read(form_len)
        s_info = list(unpack(form, s_info))
        for j in range(3):
            s_info[j] = s_info[j].decode('utf-8')
            s_info[j] = s_info[j].replace('\x00', '')
        
        if s_info[field] == bred:
            print("|{0:^25}|{1:^25}|{2:^20}|".format(s_info[0], s_info[1], str(int(s_info[2]))))
            flag = False
    f.close()
    if flag:
        print("Нет такой строчки:(")


def chek_bd(f): # проверка бд на существование
    try:
        filename = open(f, 'rb')
        filename.close()
    except FileNotFoundError:
        return False
    return True


def look_for_two(file, f1, f2, field1, field2, form_len, form): # поиск по двум полям
    flag = True
    f = open(file, 'rb')
    f.seek(0, 2)
    size = f.tell()
    f.seek(0)
    for i in range(size // form_len):
        s_info = f.read(form_len)
        s_info = list(unpack(form, s_info))
        for j in range(3):
            s_info[j] = s_info[j].decode('utf-8')
            s_info[j] = s_info[j].replace('\x00', '')
        
        if s_info[field1] == f1 and s_info[field2] == f2:
            print("|{0:^25}|{1:^25}|{2:^20}|".format(s_info[0], s_info[1], str(int(s_info[2]))))
            flag = False
    f.close()
    if flag:
        print("Нет такой строчки:(")


# def check_input(in_s):
#    mas = [in_s.split("--")]
#    if len(mas) == 3 and len(mas[2]) == 6 and not (mas[2].ifalpha()):
#        return True
#    print("Ой, повторите добавление записи)")
#    return False

s_format = "25s25s2s"
len_s_format = 52
print_menu()
file = None
curr_command = input(": ")
translater = {"Кличка": 0, "Порода": 1, "Возраст": 2}
# print(translater["Кличка"])
while curr_command != 0:
    match curr_command:
        case "0":
            print("До свидания!")
            break
        case "1":
            file = input("Введите путь к файлу: ")
        case "2":
            if file is None:
                print("Файл не был выбран")
            else:
                innit_db(file, s_format)
        case "3":
            if file is None:
                print("Файл не был выбран")
            elif chek_bd(file):
                output_bd(file, s_format, len_s_format)
            else:
                print("Ваш файл не существует")
        case "4":
            if file is None:
                print("Файл не был выбран")
            elif chek_bd(file):
                add_info(file, s_format)
            else:
                print("Ваш файл не существует")
        case "6":
            if file is None:
                print("Файл не был выбран")
            elif chek_bd(file):
                gap = input("Введите поле для поиска: 'Кличка', 'Порода', 'Возраст' --> ")
                print("Введите значение поля")
                bred = input(":> ")
                match gap:
                    case "Кличка":
                        look_for_one(file, translater[gap], bred, len_s_format, s_format)
                    case "Порода":
                        look_for_one(file, translater[gap], bred, len_s_format, s_format)
                    case "Возраст":
                        look_for_one(file, translater[gap], bred, len_s_format, s_format)
                    case _:
                        print("Такого поля нет:(")
            else:
                print("Ваш файл не существует")
        case "7":
            if file is None:
                print("Файл не был выбран")
            elif chek_bd(file):
                print("Поиск по двум полям : 'Кличка', 'Порода', 'Возраст'")
                gap1 = input("Введите поле 1 --> ")
                find1 = input("Введите значение поля 1 --> ")
                gap2 = input("Введите поле 2 --> ")
                find2 = input("Введите значение поля 2 --> ")
                try:
                    look_for_two(file, find1, find2, translater[gap1], translater[gap2], len_s_format, s_format)
                except KeyError:
                    print("Поля не распознаны. Повторите вызов команды")
            else:
                print("Ваш файл не существует")
        
        case "5":
            if file is None:
                print("Файл не был выбран")
            elif chek_bd(file):
                deleting(file, len_s_format)
            else:
                print("Ваш файл не существует")
        
        case "8":
            print_menu()
        case _:
            print("Команда не распознана")
    if curr_command != "8":
        print_menu()
    curr_command = input(": ")
