import os
import pyperclip

import string
import random


def receberTamanhoSenha():
    while True:
        try:
            user_input = int(input("Digite o tamanho da senha: "))

            if user_input < 8:
                print("A quantidade de caracteres deve ser maior ou igual à 8!!")
                continue
            if user_input > 32:
                print("A quantidade de caracteres deve ser menor do que 32!!")
                continue

            return user_input

        except ValueError:
            print("Por favor, digite apenas números!!")
            continue


def reShuffle(lista):
    for i in range(1, len(lista)):
        if result[i] == result[i - 1]:
            random.shuffle(lista)


s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

print("Valor máximo 32 caracteres!")
entrada = receberTamanhoSenha()

random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)


result = []

for x in range(part1):
    result.append(s1[x])
    result.append(s2[x])

for x in range(part2):
    result.append(s3[x])
    result.append(s4[x])


random.shuffle(result)

for i in range(1, len(result)):
    if result[i] == result[i - 1]:
        random.shuffle(result)
while True:
    for i in range(1, len(result)):
        if result[i] == result[i - 1]:
            reShuffle(result)
            continue
    break


senha = "".join(result)
print("Sua senha:", senha)

input("\nPressione [ENTER] para copiar a senha para a área de transferência...")
pyperclip.copy(senha)

os.system("cls||clear")
print("Senha copiada com sucesso!!")
