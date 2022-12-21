# Серышева Дарья ИУ7-14Б

# Требуется написать программу, которая позволит с помощью меню выполнить
# следующие действия:
# 1. Выбрать файл для работы #
# 2. Инициализировать базу данных (создать либо перезаписать файл и заполнить
# его записями) #
# 3. Вывести содержимое базы данных
# 4. Добавить запись в конец базы данных #
# 5. Поиск по одному полю
# 6. Поиск по двум полям


def print_menu():  # вывод меню
    print("Список команд для работы с текстовыми базами данных:",
          "0 -> выход из программы", "1 -> выбрать файл для работы", "2 -> инициализация бд",
          "3 -> вывод содержимого бд", "4 -> добавить запись в конец бд", "5 -> поиск по одному полю в бд",
          "6 -> поиск по двум полям бд", "7 -> повторный вывод меню", sep="\n")


def output_bd(file):
    print("|{0:^20}|{1:^20}|{2:^20}|".format('Кличка', "Порода", "Возраст (n лет)"))
    print("+", "-" * 62, "+", sep='')
    with open(file, 'r') as f:
        for line in f:
            s = line.split("--")
            s[2] = s[2].replace('\n', '')
            print("|{0:^20}|{1:^20}|{2:^20}|".format(s[0], s[1], s[2]))


def inn(str):
    s = input(str + " :> ")
    while len(s) > 20:
        print("Длина не больше 20 символов. Повторите ввод")
        s = input(str + " :> ")
    return s


def inn_age(str):
    s = input(str + " :> ")
    while not (len(s) <= 20 and s.isdecimal()):
        print("Длина не больше 20 символов и возраст - это число. Повторите ввод")
        s = input(str + " :> ")
    return s


def innit_db(file):
    n = int(input("Введите количество строк, которые хотите добавить: "))
    f = open(file, 'w')
    for i in range(n):
        print("Введите данные о собаке: кличка, порода(строчными буквами) и возраст")
        name = inn("Кличка")
        breed = inn("Порода(строчными)")
        age = inn_age("возраст(количество полных лет)")
        s = name + "--" + breed + "--" + age
        s += '\n'
        f.write(s)
    f.close()


def add_info(f):
    print("Введите данные о собаке: кличка, порода и возраст (не больше 20 сим)")
    name = inn("Кличка")
    breed = inn("Порода(строчными)")
    age = inn_age("возраст(количество полных лет)")
    s = name + "--" + breed + "--" + age + '\n'
    f = open(file, 'a')
    f.write(s)
    f.close()


def look_for_one(file, field, bred):
    flag = True
    with open(file, 'r') as f:
        for line in f:
            s = line.split("--")
            s[2] = s[2].replace('\n', '')
            if s[field] == bred:
                print("|{0:^20}|{1:^20}|{2:^20}|".format(s[0], s[1], s[2]))
                flag = False
    if flag:
        print("Нет такой строчки:(")


def chek_bd(f):
    try:
        filename = open(f, 'r')
        filename.close()
    except FileNotFoundError:
        return False
    return True


# def look_for_two(file, bred, age):
#    with open(file, 'r') as f:
#        for line in f:
#            s = line.split("--")
#            s[2] = s[2].replace('\n', '')
#            if s[1] == bred and s[2] == age:
#                print("|{0:^20}|{1:^20}|{2:^20}|".format(s[0], s[1], s[2]))

def look_for_two(file, f1, f2, field1, field2):
    flag = True
    with open(file, 'r') as f:
        for line in f:
            s = line.split("--")
            s[2] = s[2].replace('\n', '')
            if s[field1] == f1 and s[field2] == f2:
                print("|{0:^20}|{1:^20}|{2:^20}|".format(s[0], s[1], s[2]))
                flag = False
    if flag:
        print("Нет такой строчки:(")


# def check_input(in_s):
#    mas = [in_s.split("--")]
#    if len(mas) == 3 and len(mas[2]) == 6 and not (mas[2].ifalpha()):
#        return True
#    print("Ой, повторите добавление записи)")
#    return False

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
        case "1":  # Проверка ввода(!!!)
            file = input("Введите путь к файлу: ")
        case "2":
            if file is None:
                print("Файл не был выбран")
            else:
                innit_db(file)
        case "3":
            if file is None:
                print("Файл не был выбран")
            elif chek_bd(file):
                output_bd(file)
            else:
                print("Ваш файл не существует")
        case "4":
            if file is None:
                print("Файл не был выбран")
            elif chek_bd(file):
                add_info(file)
            else:
                print("Ваш файл не существует")
        case "5":
            if file is None:
                print("Файл не был выбран")
            elif chek_bd(file):
                gap = input("Введите поле для поиска: 'Кличка', 'Порода', 'Возраст' --> ")
                print("Введите значение поля")
                bred = input(":> ")
                match gap:
                    case "Кличка":
                        look_for_one(file, translater[gap], bred)
                    case "Порода":
                        look_for_one(file, translater[gap], bred)
                    case "Возраст":
                        look_for_one(file, translater[gap], bred)
                    case _:
                        print("Такого поля нет:(")
            else:
                print("Ваш файл не существует")
        case "6":
            # print("Поиск по породе и возрасту. Введите породу")
            # find_breed = input(":> ")
            # print("Введите возраст")
            # find_age = input(":> ")
            # look_for_two(file, find_breed, find_age)
            
            if file is None:
                print("Файл не был выбран")
            elif chek_bd(file):
                print("Поиск по двум полям : 'Кличка', 'Порода', 'Возраст'")
                gap1 = input("Введите поле 1 --> ")
                find1 = input("Введите значение поля 1 --> ")
                gap2 = input("Введите поле 2 --> ")
                find2 = input("Введите значение поля 2 --> ")
                try:
                    look_for_two(file, find1, find2, translater[gap1], translater[gap2])
                except KeyError:
                    print("Поля не распознаны. Повторите вызов команды")
            else:
                print("Ваш файл не существует")
        
        case "7":
            print_menu()
        case _:
            print("Команда не распознана")
    print_menu()
    curr_command = input(": ")
