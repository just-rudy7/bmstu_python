# Серышева ИУ7-14Б
# Необходимо реализовать ввод в файл(или перезапись, потом удалить все отрицательные элементы
# 5 и 3

from struct import *
from addiction import *


def delete_negative(file, form, form_len):
    f = open(file, 'rb+')
    f.seek(0, 2)
    size = f.tell() // 4  # количество записей
    f.seek(0)
    i = 0
    shift = 0  # сдвиг влево всех записей (для удаления перезаписью)
    while i+shift < size:
        f.seek(i * form_len)
        num = int(unpack(form, f.read(form_len))[0])
        if num < 0: #TODO проверяй, есть ли числа после
            shift += 1
            if i+shift < size:
                f.seek((i + shift) * form_len)
                tmp = f.read(4)
                #print(type(tmp))
                #print(tmp)
                tmp = list(unpack(form, tmp))
                #print(tmp)
                f.seek(i * form_len)
                f.write(pack(form, tmp[0]))
            else:
                i = size
        else:
            i += 1
        #print(shift)
    
    f.truncate((size-shift) * form_len)
    f.close()


file = choose_file()
innit_file(file, "i")

delete_negative(file, "i", 4)

output_file(file, "i", 4)
