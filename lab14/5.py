string = input()
nach = int(input())
kon = int(input())
number = string[nach:kon+1]
alf = "1234567890"
is_number = True

if not(number[0] == "-" or number[0] in alf):
    is_number = False
for i in range(1, len(number)):
    if number[i] not in alf:
        is_number = False

if is_number:
    print("Подстрока - число")
    print()
else:
    print("Не число")