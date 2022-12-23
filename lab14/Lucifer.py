# пока без начальных и конечных перестановок, но модет как-нибудь
from struct import pack as pack
from struct import unpack as unpack
from make_a_key import key_changing as shift_key


def f_for_des(r, k):
    r_new = 0
    return r_new


def code(file_name):
    f = open(file_name, 'rb+')
    for i in range(1, 17):
        bin_key = shift_key(i)
    
    ciphertext = ""
    f.close()


def decode(ciphertext):
    text = ""
    return text


code("1.bin")
