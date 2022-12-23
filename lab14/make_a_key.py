from struct import pack as pack
from struct import unpack as unpack


# перестановка ключа со сжатием до 56 битов
def reorganize_first_time(bin_key):
    new_bin_key = ""
    for i in range(57, 0, -8):
        new_bin_key += bin_key[i]
    for i in range(58, 0, -8):
        new_bin_key += bin_key[i]
    for i in range(59, 0, -8):
        new_bin_key += bin_key[i]
    for i in range(60, 35, -8):
        new_bin_key += bin_key[i]
    for i in range(63, 0, -8):
        new_bin_key += bin_key[i]
    for i in range(62, 0, -8):
        new_bin_key += bin_key[i]
    for i in range(61, 0, -8):
        new_bin_key += bin_key[i]
    for i in range(28, 0, -8):
        new_bin_key += bin_key[i]

    # print(new_bin_key, len(new_bin_key))
    
    return bin_key


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
    f.write(pack("16s", key.encode("utf-8")))
    bin_key = ""
    for x in key:
        bin_key += '{0:04b}'.format(int(x, 16))
    
    bin_key = reorganize_first_time(bin_key)
    f.seek(0, 2)
    f.write(pack("56s", bin_key.encode("utf-8")))
    f.close()


def key_changing(stage):
    f = open("key.bin", "rb")
    f.seek(16)
    bin_key = (unpack("56s", f.read(56))[0]).decode('utf-8', errors='ignore')
    if stage <= 2 or stage == 9 or stage == 16:
        shift = 1
    else:
        shift = 2
    r_key = bin_key[:28]
    l_key = bin_key[28:]
    new_key = ""
    return new_key

# key_changing(1)