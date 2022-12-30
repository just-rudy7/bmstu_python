from struct import pack as pack
from struct import unpack as unpack
from make_a_key import key_changing as shift_key


def change_positions_for_a_start(text):
    new_text = ""
    cnt = 0
    for i in range(58, 0, -8):
        new_text += text[i - 1]
    for i in range(60, 0, -8):
        new_text += text[i - 1]
    for i in range(62, 0, -8):
        new_text += text[i - 1]
    for i in range(64, 0, -8):
        new_text += text[i - 1]
    for i in range(57, 0, -8):
        new_text += text[i - 1]
    for i in range(59, 0, -8):
        new_text += text[i - 1]
    for i in range(61, 0, -8):
        new_text += text[i - 1]
    for i in range(63, 0, -8):
        new_text += text[i - 1]
    return new_text


def change_positions_for_an_end(text):
    new_text = ""
    L = 40
    r = 8
    while L <= 64 and r <= 32:
        new_text += text[L - 1] + text[r - 1]
        L += 8
        r += 8
    L = 39
    r = 7
    while L <= 64 and r <= 31:
        new_text += text[L - 1] + text[r - 1]
        L += 8
        r += 8
    L = 38
    r = 6
    while L <= 62 and r <= 30:
        new_text += text[L - 1] + text[r - 1]
        L += 8
        r += 8
    L = 37
    r = 5
    while L <= 61 and r <= 29:
        new_text += text[L - 1] + text[r - 1]
        L += 8
        r += 8
    L = 36
    r = 4
    while L <= 60 and r <= 28:
        new_text += text[L - 1] + text[r - 1]
        L += 8
        r += 8
    L = 35
    r = 3
    while L <= 59 and r <= 27:
        new_text += text[L - 1] + text[r - 1]
        L += 8
        r += 8
    L = 34
    r = 2
    while L <= 58 and r <= 26:
        new_text += text[L - 1] + text[r - 1]
        L += 8
        r += 8
    L = 33
    r = 1
    while L <= 57 and r <= 25:
        new_text += text[L - 1] + text[r - 1]
        L += 8
        r += 8
    return new_text


def f_for_des(r, k):
    r_new = 0
    return r_new


def rearrange_extantion(text):
    print(text)
    new = ""
    mas = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21,
           20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]
    
    for i in mas:
        new += text[i - 1]
    return new


def choose_s(step):
    match step:
        case 1:
            return [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
                    [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
                    [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
                    [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]
        case 2:
            return [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
                    [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
                    [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
                    [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]]
        case 3:
            return [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
                    [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
                    [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
                    [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]]
        case 4:
            return [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
                    [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
                    [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
                    [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]]
        case 5:
            return [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
                    [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
                    [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
                    [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]]
        case 6:
            return [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
                    [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
                    [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
                    [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]]
        case 7:
            return [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
                    [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
                    [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
                    [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]]
        case 8:
            return [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
                    [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
                    [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
                    [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]


def s(text):
    new_text = ""
    print(text)
    for i in range(0, len(text) - 5, 6):
        string = text[i:i + 6]
        s_b = choose_s(i // 6 + 1)
        text_s = bin(s_b[int(string[0] + string[5], 2)][int(string[1:5], 2)])[2:]
        text_s = "0" * (4 - len(text_s)) + text_s
        new_text += text_s
        # print(string, "=-=", text_s)
    return new_text


def p_block(text):
    rearr = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10,
             2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]
    new_text = ""
    for i in rearr:
        new_text += text[i - 1]
    return new_text


def xor(a, b):
    new = ""
    for i in range(len(a)):
        if a[i] != b[i]:
            new += "1"
        else:
            new += "0"
    return new


def code(text):
    # ciphertext = ""
    new_text = ""
    # for x in text:
    #     ciphertext += str(hex(ord(x)))[2:]
    # ciphertext += "0" * (8 - len(ciphertext) % TODO bring bqck
    ciphertext = "0123456789ABCDEF"
    ciphertext_bin = ""
    for x in ciphertext:
        ciphertext_bin += '{0:04b}'.format(int(x, 16))
    for piece in range(0, len(ciphertext_bin) // 64):
        # some_string = ciphertext_bin[piece * 64:(piece + 1) * 64]
        code_text = ciphertext_bin[piece * 64:(piece + 1) * 64]
        print("==--==", code_text, len(code_text), "==--==") # TODO wrong l r
        code_text = change_positions_for_a_start(code_text)
        print("start: ", code_text, len(code_text))
        l_t = code_text[:32]
        r_t = code_text[32:]
        for i in range(1, 17):
            print("1:", r_t)
            r1_t = xor(rearrange_extantion(r_t), shift_key(i))  # TODO перестает быть bin
            print("2:", r1_t)
            r1_t = p_block(s(r1_t))
            r1_t = str(xor(r1_t, l_t))
            l_t = r_t
            r_t = r1_t
        new_text += change_positions_for_an_end(r_t + l_t)
    return new_text


def decode(ciphertext):
    text = ""
    return text


print(code("0123456789ABCDEF"))
