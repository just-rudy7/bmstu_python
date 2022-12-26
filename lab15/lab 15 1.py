# Серышева ИУ7-14Б
# Необходимо реализовать ввод в файл(или перезапись, потом удалить все отрицательные элементы
# 5 и 3

from struct import *
from addiction import *


def delete_negative(file, form, form_len):
    f = open(file, 'rb+')
    f.seek(0, 2)
    size = f.tell() // form_len  # количество записей
    f.seek(0)
    cnt_left = 0
    for i in range(size):
        f.seek(i*form_len)
        num = int(unpack(form, f.read(form_len))[0])
        if num > 0:
            f.seek(cnt_left*form_len)
            f.write(pack(form, num))
            cnt_left += 1
            
    f.truncate(cnt_left * form_len)
    f.close()


file = choose_file()
innit_file(file, "i")

delete_negative(file, "i", 4)

output_file(file, "i", 4)