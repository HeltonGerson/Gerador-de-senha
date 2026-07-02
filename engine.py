import os
import string
import random
import pyperclip
from datetime import datetime


def limparTela():
    os.system("cls||clear")


def copiar(senha):
    input("\nPressione [ENTER] para copiar a senha para a área de transferência...")
    pyperclip.copy(senha)


def receberTamanhoSenha():
    while True:
        print("Valor máximo: 32 caracteres!\nValor mínimo: 8 caracteres!\n")
        try:
            user_input = int(input("Digite o tamanho da senha: "))

            if user_input < 8:
                print("A quantidade de caracteres deve ser maior ou igual à 8!!")
                input("Pressione [ENTER] para continuar!")
                limparTela()
                continue
            if user_input > 32:
                print("A quantidade de caracteres deve ser menor ou igual à 32!!")
                input("Pressione [ENTER] para continuar!")
                limparTela()
                continue

            return user_input

        except ValueError:
            print("Por favor, digite apenas números!!")
            input("Pressione [ENTER] para continuar!")
            limparTela()
            continue


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


def checarRepeticao(senhaGerada):
    while True:
        for i in range(1, len(senhaGerada)):
            if senhaGerada[i] == senhaGerada[i - 1]:
                random.shuffle(senhaGerada)
                continue
        break


def salvarSenha(senhaGerada):
    senha = "".join(senhaGerada)

    historico = {}

    agora_formatado = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    historico[agora_formatado] = senha

    with open("historico.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{agora_formatado} = ")
        arquivo.write(f"{historico[agora_formatado]}\n")
