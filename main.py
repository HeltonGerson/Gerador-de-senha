import engine

import os
import pyperclip

entrada = engine.receberTamanhoSenha()

senhaGerada = engine.gerador(entrada)

while True:
    for i in range(1, len(senhaGerada)):
        if senhaGerada[i] == senhaGerada[i - 1]:
            engine.reShuffle(senhaGerada)
            continue
    break

senha = "".join(senhaGerada)

print("Sua senha:", senha)

input("\nPressione [ENTER] para copiar a senha para a área de transferência...")
pyperclip.copy(senha)

os.system("cls||clear")
print("Senha copiada com sucesso!!")
