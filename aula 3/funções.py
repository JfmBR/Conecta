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

"""
def calcular_frete(peso,distancia_km,expresso = False):
    frete = (peso * 2) + (distancia_km * 0.5)
    if expresso == True:
        frete *= 2
        print(f"Valor do frete: {frete}")
    else:
        print(f"valor do frete: {frete}")
    
calcular_frete(50,100, True)"""

"""
def calcular_total(valores:list):
    if valores == []:
        return None
    total = sum(valores)
    return total

print(calcular_total([200,20,50,40,50]))"""

"""
def triangulo_validor(a,b,c):
    lado = sorted([a,b,c])
    if lado[0] + lado[1] <= lado[2]:
        return "Não é um triangulo"
    elif a == b == c:
        return "Equilatero"
    elif a == b or b == c or c == a:
        return "Isoceles"
print(triangulo_validor(1,2,3))
print(triangulo_validor(1,8,8))
print(triangulo_validor(3,3,3))"""

"""
contador_global = 0

def incremento():
    global contador_global
    contador_global += 1
    resultado_local = contador_global * 2
    return resultado_local

print (incremento())
print (incremento())"""

"""
def pedir_numero(mensagem, minimo = None, maximo = None, tipo = float):
    while True:
        try:
            valor = tipo(input(mensagem))
            if minimo is not None and valor < minimo:
                print (f"Valor deve ser >= {minimo}.");continue
            elif maximo is not None and valor > maximo:
                print(f"valor deve ser <= {maximo}.");continue
            return valor
        except ValueError:
            print("Entrada invalida. Digite um numero valido")

preco = pedir_numero("Preco (R$):", minimo = 0.01)
print (preco)
"""
"""
def dividir_seguro(a,b):
    if b == 0:
        return None
    else:
        resultado = a / b
        return resultado
"""

def estatisticas(lista:list):
    soma = sum(lista)
    media = sum(lista) / len(lista)
    maior = max(lista)
    minimo = min(lista)
    return soma, media, maior, minimo
resultado = estatisticas([32,50,80,50])
print (resultado)