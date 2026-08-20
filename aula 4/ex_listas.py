"""
numeros = [3,7,1,9,4]
print(numeros[0:3])
print(numeros[: : -2])

resultado = [x * 2 for x in range(10) if x % 3 == 0]
print(resultado)

quadrados_impares = [x**2 for x in range(1,20) if x % 2 != 0]
print(quadrados_impares)

dados_vendas = [120.5,89.9,340.0,15.0,220.0]
media = round(sum(dados_vendas) / len(dados_vendas), 2)
Venda_metas = [x for x in dados_vendas if x >= media]
print(media)
print(Venda_metas)

resultado = []
for i in range (1,21):
    if i % 2 != 0:
        i = i ** 2
        resultado.append(i)
print(resultado)"""
