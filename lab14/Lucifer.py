# пока без начальных и конечных перестановок, но модет как-нибудь
from struct import pack as pack
from struct import unpack as unpack
from make_a_key import key_changing as shift_key


def change_positions_for_a_start(text):
    new_text = ""
    for i in range(58 - 1, 0, -8):
        new_text += text[i]
    for i in range(60 - 1, 0, -8):
        new_text += text[i]
    for i in range(62 - 1, 0, -8):
        new_text += text[i]
    for i in range(64 - 1, 0, -8):
        new_text += text[i]
    for i in range(57 - 1, 0, -8):
        new_text += text[i]
    for i in range(59 - 1, 0, -8):
        new_text += text[i]
    for i in range(61 - 1, 0, -8):
        new_text += text[i]
    for i in range(63 - 1, 0, -8):
        new_text += text[i]
    return new_text


def f_for_des(r, k):
    r_new = 0
    return r_new


def rearrange_extantion(text):
    new = ""
    mas = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21,
           20, 21,
           22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]
    
    for i in mas:
        new += text[i - 1]
    return new


def s(text):
    

def code(text):
    ciphertext = ""
    for x in text:
        ciphertext += str(hex(ord(x)))[2:]
    print(len(ciphertext), ciphertext)
    ciphertext += "0" * (8 - len(ciphertext) % 8)
    
    ciphertext_bin = ""
    for x in ciphertext:
        ciphertext_bin += '{0:04b}'.format(int(x, 16))
    for piece in range(0, len(ciphertext_bin) // 64):
        code_text = ciphertext[piece * 64:(piece + 1) * 64]
        code_text = change_positions_for_a_start(code_text)
        l_text = code_text[:32]
        r_text = code_text[32:]
        for i in range(1, 17):
            l1_text = r_text
            r1_text = str(int(rearrange_extantion(r_text)) ^ int(shift_key(i)))
            r1 = s(r1)
    
    return ciphertext


def decode(ciphertext):
    text = ""
    return text


code("Your lips are smother than vaseline. ")
