#Ordem de resolução: not - and - or
#print ((23 % 7.23) // (7.2 ** 10))

'''
idade = 15
print (not(idade<18))
idade = 20
print (not(idade<20))
'''

'''
nota = 8.0
status = "aprovado" if nota >=7.0 else "reprovado"
print (status)
'''

'''
x = int(input())
sinal = "positivo" if x>0 else "não positivo"
print (sinal)
'''

'''
idade = int(input())

if idade < 12:
    print("Criança")
    print("brinquedo")

elif idade >= 12 and idade < 18:
    print("adolescente")

else:    
    print("Adulto")
'''
'''
while True:

    try:
        numero = int(input("Digite um numero: "))
        resultado = 100 / numero

    except ValueError:
        print("Não é um numero válido")

    except ZeroDivisionError:
        print("Zero não é um numero divisivel")

    else:
        print(f"Tudo Certo!!!\nO resultado da divisão é: {resultado}")
        break

    finally:
        print("Progama finalizou")
'''

"""valores = [1,2,3,4,5,6,7,8,9,]

print(f"Quantidade de Elementos: {len(valores)}")
print(f"Soma de todos os valores:{sum(valores)}")
print(f"Minimo: {min(valores)}")
print(f"Maximo: {max(valores)}")"""

'''
funcionario = ["Ana", "Bianca", "Beatriz"]
venda = [1200, 800, 1000]
meta = [1000, 1000, 1000]

for funcionario, venda, meta in zip(funcionario,venda,meta):
    status = "meta atingida" if venda >= meta else "meta não atingida"
    print(f"{funcionario} : {status}")
'''

'''
regiao = ["Norte", "Sul"]
trimestre = ["1", "2", "3"]

for i in regiao:
    for y in trimestre:
        print(f"{i} : {y}")
'''


'''tentativa_restantes = 3
senha_correta = "python123"

while tentativa_restantes > 0:
    senha =  input("Digite sua senha: ")
    if senha == senha_correta:
        print("Acessando...")
        break
    tentativa_restantes -= 1
    print(tentativa_restantes)
else:
    print ("Tentativas acabaram")'''
soma = 0
for i in range(1 ,101):
    print (soma)
    soma += i

