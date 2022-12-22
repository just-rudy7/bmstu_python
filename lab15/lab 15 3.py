# Серышева ИУ7-14Б
# Реализовать сортировку пузырьком с флагом

from struct import *
from addiction import *


def bubble_sort(file, form, form_len, dir):
    f = open(file, 'rb+')
    f.seek(0, 2)
    size = f.tell() // form_len
    f.seek(0)
    if_sorted = False
    while not if_sorted:
        if_sorted = True
        for i in range(1, size):
            f.seek((i-1)*form_len)
            el1 = int(unpack(form, f.read(form_len))[0])
            f.seek(i*form_len)
            el2 = int(unpack(form, f.read(form_len))[0])
 
            if el1 * dir < el2 * dir:
                if_sorted = False
                f.seek((i - 1) * form_len)
                f.write(pack(form, el2))
                f.seek(i * form_len)
                f.write(pack(form, el1))
    f.close()


file = choose_file()
innit_file(file, "i")

print("Выберите направление сортировки")
factor = 2
while factor != 1 and factor != -1:
    try:
        factor = int(input("'1' - по убыванию, '-1' - по возрастанию :> "))
    except ValueError:
        pass


bubble_sort(file, "i", 4, factor)

output_file(file, "i", 4)
