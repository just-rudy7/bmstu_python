s = ["", "", "", ""]
for j in range(4):
    for i in range(16):
        tmp = input()
        s[j] += tmp + ", "
    print(s[j])
print(s)
