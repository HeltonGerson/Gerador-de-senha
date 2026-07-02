import engine

import os
import pyperclip

entrada = engine.receberTamanhoSenha()

senhaGerada = engine.gerador(entrada)

engine.checarRepeticao(senhaGerada)

senha = "".join(senhaGerada)

print("Sua senha:", senha)

input("\nPressione [ENTER] para copiar a senha para a área de transferência...")
pyperclip.copy(senha)

os.system("cls||clear")
print("Senha copiada com sucesso!!")
