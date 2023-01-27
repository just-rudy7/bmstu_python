# def insert_sort(mas):
#     for i in range(1, len(mas)):
#         j = i - 1
#         tmp = mas[i]
#         while tmp < mas[j] and j >= 0:
#             mas[j+1] = mas[j]
#             j -= 1
#         mas[j+1] = tmp
#     return mas

# def selection_sort(mas):
#     end = len(mas)
#     for i in range(len(mas)):
#         i_max = 0
#         mx = mas[0]
#         for j in range(0, end):
#             if mas[j] > mx:
#                 mx = mas[j]
#                 i_max = j
#         mas[end-1], mas[i_max] = mas[i_max], mas[end-1]
#         end -= 1
#     return mas

def inserte_binary(mas):
    for i in range(len(mas)):
        tmp = mas[i]
        l, r = 0, i
        while l < r:
            mid = (l + r)//2
            if tmp >= mas[mid]:
                l = mid+1
            else:
                r = mid
        for j in range(i, l, -1):
            mas[j] = mas[j-1]
        mas[l] = tmp
    return mas


def insert_barrier(mas):
    mas = [0] + mas
    for i in range(2, len(mas)):
        if mas[i-1] > mas[i]:
            mas[0] = mas[i]
            j = i - 1
            while mas[j] > mas[0]:
                mas[j+1] = mas[j]
                j -= 1
            mas[j+1] = mas[0]
    return mas[1:]


def shell(mas):
    dif = len(mas) // 2
    while dif:
        for i, el in enumerate(mas):
            while i > dif and mas[i-dif] > el:
                mas[i] = mas[i-dif]
                i -= dif
            mas[i] = el
        dif = 1 if dif == 2 else int(dif*5.0/11)
    return mas


#mas = list(map(int, input().split()))
#print(shell(mas))

mas = [1, 2, 'jim', ['pam']]
del mas[0]
print(mas)