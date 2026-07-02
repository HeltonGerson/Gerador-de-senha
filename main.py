import engine

entrada = engine.receberTamanhoSenha()

senhaGerada = engine.gerador(entrada)

engine.checarRepeticao(senhaGerada)

engine.salvarSenha(senhaGerada)

senha = "".join(senhaGerada)

print("Sua senha:", senha)

engine.copiar(senha)

engine.limparTela()
print("Senha copiada com sucesso!!")
