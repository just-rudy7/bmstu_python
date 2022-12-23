frases = input("Введите предложения: ")
alf_small = "qwertyuiopasdfghjklzxcvbnmйцукенгшщзхъфывапролджэячсмитьбюё"
alf_big = "QWERTYUIOPASDFGHJKLZXCVBNMЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ"

if_dot = True
for i in range(len(frases)):
    if if_dot and frases[i] in alf_small:
        frases = frases[:i] + alf_big[alf_small.find(frases[i])] + frases[i+1:]
        if_dot = False
    elif frases[i] == ".":
        if_dot = True

print(frases)