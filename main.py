import os
import pyperclip

import string
import random


def receberTamanhoSenha():
    while True:
        print("Valor máximo: 32 caracteres!\nValor mínimo: 8 caracteres!\n")
        try:
            user_input = int(input("Digite o tamanho da senha: "))

            if user_input < 8:
                print("A quantidade de caracteres deve ser maior ou igual à 8!!")
                input("Pressione [ENTER] para continuar!")
                os.system("cls||clear")
                continue
            if user_input > 32:
                print("A quantidade de caracteres deve ser menor do que 32!!")
                input("Pressione [ENTER] para continuar!")
                os.system("cls||clear")
                continue

            return user_input

        except ValueError:
            print("Por favor, digite apenas números!!")
            input("Pressione [ENTER] para continuar!")
            os.system("cls||clear")
            continue


def reShuffle(lista):
    for i in range(1, len(lista)):
        if lista[i] == lista[i - 1]:
            random.shuffle(lista)


def gerador(entrada):
    s1 = list(string.ascii_lowercase)
    s2 = list(string.ascii_uppercase)
    s3 = list(string.digits)
    s4 = list(string.punctuation)

    random.shuffle(s1)
    random.shuffle(s2)
    random.shuffle(s3)
    random.shuffle(s4)

    part1 = round(entrada * (30 / 100))
    part2 = round(entrada * (20 / 100))

    result = []

    for x in range(part1):
        result.append(s1[x])
        result.append(s2[x])

    for x in range(part2):
        result.append(s3[x])
        result.append(s4[x])

    random.shuffle(result)

    return result


entrada = receberTamanhoSenha()

senhaGerada = gerador(entrada)

while True:
    for i in range(1, len(senhaGerada)):
        if senhaGerada[i] == senhaGerada[i - 1]:
            reShuffle(senhaGerada)
            continue
    break

senha = "".join(senhaGerada)

print("Sua senha:", senha)

input("\nPressione [ENTER] para copiar a senha para a área de transferência...")
pyperclip.copy(senha)

os.system("cls||clear")
print("Senha copiada com sucesso!!")
