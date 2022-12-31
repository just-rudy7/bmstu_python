from struct import pack as pack
from struct import unpack as unpack


# перестановка ключа со сжатием до 56 битов
def reorganize_first_time(bin_key):
    new_bin_key = ""
    for i in range(57, 0, -8):
        new_bin_key += bin_key[i - 1]
    for i in range(58, 0, -8):
        new_bin_key += bin_key[i - 1]
    for i in range(59, 0, -8):
        new_bin_key += bin_key[i - 1]
    for i in range(60, 35, -8):
        new_bin_key += bin_key[i - 1]
    for i in range(63, 0, -8):
        new_bin_key += bin_key[i - 1]
    for i in range(62, 0, -8):
        new_bin_key += bin_key[i - 1]
    for i in range(61, 0, -8):
        new_bin_key += bin_key[i - 1]
    for i in range(28, 0, -8):
        new_bin_key += bin_key[i - 1]

    # print(new_bin_key, len(new_bin_key), 1)
    
    return new_bin_key


# Перестановка со сжатием. Не запоминаю, но передаю в key_change, а потом и в Lucifer
def choose_48(key):
    another_str = ""
    indexes = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37,
               47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]
    for i in indexes:
        another_str += key[i - 1]
    return another_str


# переопределяет ключ по требованию пользователя
def reset_your_key():
    file = "key.bin"
    f = open(file, 'wb')
    
    key = input("Введите ключ (0123456789ABCDEF) :<0 для ключа по умолчанию>: ")
    match key:
        case "0":
            key = "B7F49A07C61C0097"
        case _:
            key_size = len(key)
            if key_size < 16:
                key = "0" * (16 - key_size) + key
            elif key_size > 16:
                key = key[:16]
    bin_key = ""
    for x in key:
        bin_key += '{0:04b}'.format(int(x, 16))
    # print(bin_key)
    bin_key = reorganize_first_time(bin_key)
    # f.write(pack("56s", bin_key.encode("utf-8")))
    # f.close()
    return bin_key


# сдвиг ключа, запись его в файл, потом перестановка со сжатием до 48 бит, передача результата в Luci
def key_changing(stage, bin_key):
    # f = open("key.bin", "rb+")
    # f.seek(0)
    # bin_key = (unpack("56s", f.read(56))[0]).decode('utf-8', errors='ignore')
    # f.close()
    if stage <= 2 or stage == 9 or stage == 16:
        shift = 1
    else:
        shift = 2  # 133457799BBCDFF1
    # print("bin:", bin_key)
    l_key = bin_key[:28]
    # print("left:", l_key)
    r_key = bin_key[28:]
    # print("righ:", r_key)
    new_key = l_key[shift:] + l_key[:shift] + r_key[shift:] + r_key[:shift]
    # print("left:", l_key[shift:] + l_key[:shift])
    # print("left:", r_key[shift:] + r_key[:shift])
    # # print(new_key, len(new_key))
    # f = open("key.bin", "wb")
    # f.write(pack("56s", new_key.encode('utf-8')))
    # f.close()
    # new_key = choose_48(new_key)
    return new_key


# num = key_changing(1)
# reset_your_key()
# for i in range(1, 17):
# print("key48 =", key_changing(i))
