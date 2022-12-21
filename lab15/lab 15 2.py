# # Серышева ИУ7-14Б
# После каждого нечетного числа добавить его удвоенное
# значение (допускается два прохода по файлу)

from struct import *
from addiction import *


def add_nums(file, form, form_len):
    f = open(file, 'rb+')
    f.seek(0, 2)
    size = f.tell() // 4  # количество чисел
    cnt_odd_nums = 0  # количество нечетных чисел (= количество чисел, которые добавляем)
    
    # в этой части ф-и считаем количество нечетных и в конец файла добавляем для каждого числа его удвоенное значение
    for i in range(size):
        f.seek(i * form_len)
        num = int(unpack(form, f.read(form_len))[0])
        if num % 2 != 0:
            cnt_odd_nums += 1
            f.seek(0, 2)
            f.write(pack(form, num * 2))
    
    # а тут двигаем влево все добавленные числа, расставляя по местам
    i = 1
    while cnt_odd_nums > 0:
        ind_tmp = (size - i) * form_len
        f.seek(ind_tmp)
        tmp = int(unpack(form, f.read(form_len))[0])
        if tmp % 2 != 0:
            cnt_odd_nums -= 1
        for shift in range(cnt_odd_nums):  # TODO менять места перестановок. передавать "координату" tmp вместе с tmp
            ind_shift = (size - i + shift + 1) * form_len
            f.seek(ind_shift)
            shift_tmp = int(unpack(form, f.read(form_len))[0])
            
            f.seek(ind_shift)
            f.write(pack(form, tmp))
            
            f.seek(ind_tmp)
            f.write(pack(form, shift_tmp))
            
            ind_tmp = ind_shift
            # f.close()
            # output_file(file, form, 4)
            # f = open(file, 'rb+')
        i += 1
    f.close()


file = choose_file()
innit_file(file, "i")

add_nums(file, "i", 4)

output_file(file, "i", 4)
