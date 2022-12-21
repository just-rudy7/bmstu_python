from struct import *

form = "i"


def choose_file():
    file = input("Введите путь к файлу: ")
    return file


# ввод числа
def inn_num(str):  # проверка ввода на число
    s = None
    while s is None:
        try:
            s = int(input(str + " :> "))
        except ValueError:
            pass
    return int(s)


# инициализация (обнуление файла и добавление какого-то числа записей)
def innit_file(file, form):  # иннициализация
    n = int(input("Введите количество чисел, которые хотите добавить: "))
    f = open(file, 'wb')
    for i in range(n):
        num = inn_num("Введите {0} число".format(i+1))
        s = pack(form, num)
        f.write(s)
    f.close()


# вывод чисел из файла на экран
def output_file(file, form, form_len):  # вывод
    print("|Номер     |{0:^20}|".format("Число"))
    print("+","-"*31,"+", sep="")
    f = open(file, 'rb')
    f.seek(0, 2)
    size = f.tell()
    f.seek(0)
    for i in range(size // form_len):
        s_info = f.read(form_len)
        s_info = list(unpack(form, s_info))
        print("|{0:<10}|{1:^20}|".format(i + 1, str(s_info[0])))

# 
# Nizima (Niletto)
# Nezima
# Ласты Кристмаса
# Полный Джингл Бэллс
#
