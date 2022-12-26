# # Серышева ИУ7-14Б
# После каждого нечетного числа добавить его удвоенное
# значение (допускается два прохода по файлу)

from struct import *
from addiction import *


def add_nums(file, form, form_len):
    f = open(file, 'rb+')
    f.seek(0, 2)
    size = f.tell() // form_len  # количество чисел
    cnt_odd_nums = 0  # количество нечетных чисел (= количество чисел, которые добавляем)
    
    # в этой части ф-и считаем количество нечетных и в конец файла добавляем для каждого числа его удвоенное значение
    for i in range(size):
        f.seek(i * form_len)
        num = int(unpack(form, f.read(form_len))[0])
        if num % 2 != 0:
            cnt_odd_nums += 1
            f.seek(0, 2)
            f.write(pack(form, num * 2))
    
    i = 0
    n = size + cnt_odd_nums
    print(n)
    while cnt_odd_nums > 0:
        f.seek((n-cnt_odd_nums-1-i)*form_len)
        num = int(unpack(form, f.read(form_len))[0])
        if num % 2 == 1:
            f.seek((n-2-i)*form_len)
            f.write(pack(form, num))
            f.write(pack(form, num*2))
            cnt_odd_nums -= 1
            i += 2
        else:
            f.seek((n-1-i)*form_len)
            f.write(pack(form, num))
            i += 1
    f.close()


file = choose_file()
innit_file(file, "i")

add_nums(file, "i", 4)

output_file(file, "i", 4)
