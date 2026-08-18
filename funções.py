"""
def exibir_cabeçalho(titulo):
    largura = len(titulo) + 4
    print("=" * largura)
    print(f"{titulo}")
    print("=" * largura)

exibir_cabeçalho("Olá, mundo")"""

"""
def formatar_moeda(valor,prefixo,casas):
    print(f"{prefixo}{valor:.{casas}f}")

formatar_moeda(2000,"R$",2)"""

"""
def exibir_produto(nome,preco,categoria = "Geral",estoque = 0):
    print(f"Nome do produto: {nome}")
    print(f"Preço do produro: {preco:.{2}f}")
    print(f"Categoria: {categoria}")
    print(f"Quantidade em estoque: {estoque}")

exibir_produto("Notebook", 2500,)
exibir_produto("Computador", 5000,"Eletrônico",500)"""

"""
def saudacao(nome, saudacao = "Olá"):
    print(f"{saudacao} {nome}")
saudacao("joao")
"""

def calcular_frete(peso,distancia_km,expresso = False):
    frete = (peso * 2) + (distancia_km * 0.5)
    if expresso == True:
        frete *= 2
        print(f"Valor do frete: {frete}")
    else:
        print(f"valor do frete: {frete}")
    
calcular_frete(50,100, True)