with open("log.txt", "w", encoding="UTF = 8") as arquivo:
    arquivo.write("Inicializando o arquivo por código")

with open("log.txt", "r", encoding="UTF = 8") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

