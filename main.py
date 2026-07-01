import string
import random

s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

print("Valor máximo 32 caracteres!")

while True:
    try:
        user_input = int(input("Digite o tamanho da senha: "))

        if user_input <= 8:
            print("A quantidade de caracteres deve ser maior do que 8!!")
            continue
        else:
            break

    except ValueError:
        print("Por favor, digite apenas números!!")
        continue

random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)


part1 = round(user_input * (30 / 100))
part2 = round(user_input * (20 / 100))

result = []

for x in range(part1):
    result.append(s1[x])
    result.append(s2[x])

for x in range(part2):
    result.append(s3[x])
    result.append(s4[x])


random.shuffle(result)


password = "".join(result)
print("Sua senha:", password)
