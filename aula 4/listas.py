import csv
""""
tarefas = ["ler e-mails", "Gerar relatorios"]
tarefas.append("Enviar relatorios")  #adiciona 1 item
tarefas.extend(["Arquivar", "Notificar"]) #adiciona varios
tarefas.insert(0, "Fazer backup") #insere em posição
tarefas.remove("ler e-mails") #remove pelo item
print(tarefas)
item = tarefas.pop(2) #remove desejado e retorna
print(item)
print(tarefas)"""

"""
meses = ["jan", "fev", "mar", "abr", "mai", "jun"]
#lista[inicio,fim,passos] -- fim não é incluso
primeiro_trimestre = meses[0:3] #[jan,fev,mar]
ultimos_dois = meses[-2:] #[mai, jun]
invertida = meses[: :-1] """
"""
lista = []
for i in range(1,6):
    lista.append(i)
print (lista)

lista1 = [i for i in range(1,7)]
print(lista1)

pares = [n for n in range(1,11) if n % 2 ==0]
print(pares)
"""
"""
cliente = {
    "id": 1042,
    "Nome": "Ana Carla",
    "email":"ana.mender@gmail.com",
    "plano": "Premium",
}

print(cliente["Nome"])
print(cliente.get("plano"))
print(cliente.get("cidade", "não informado"))
print(cliente)

print(cliente.keys())
print(cliente.values())
print(cliente.items())

for chave,valor in cliente:
    print(f"Chave: {chave}\nvalor: {valor}")


def obter_dimensões(texto):
    return len(texto), len(texto.split())
chars, palavras = obter_dimensões("Olá, mundo")

palavra = "olá Mundo"

print(palavra.split("o"))
"""
"""
extensoes = {".csv", ".xlsx", ".csv", ".json", ".xlsx"}

#print (extensoes)  #não duplica
planilhas = {".csv", ".xlsx", ".ods"}
documentos = {".pdf",".dock", ".xlsx"}
comum = planilhas & documentos
todos = planilhas | documentos
print(comum)
print(todos)
"""

registros = [
    {"Nome":"Carlos", "Departamento":"TI", "Salario": 5000.00},
    {"Nome":"Ana", "Departamento":"RH", "Salario": 5200.00},
    {"Nome":"João", "Departamento":"Financeiro", "Salario": 7000.00},
    {"Nome":"Pedro", "Departamento":"TI", "Salario": 5000.01}
]
"""
salario_ti =[]
for registros in registros:
    if registros["Departamento"] == registros["TI"]:
        salario_ti.append(registros)
print(salario_ti)
"""
with open("funcionarios.csv", "w", newline= "", encoding= "UTF = 8")as arquivo:
    campos = ["Nome", "Departamento", "Salario"]
    escritor = csv.DictWriter(arquivo,fieldnames=campos)
    escritor.writeheader()
    escritor.writerows(registros)

with open("funcionarios.csv", "r", encoding="UTF=8") as arquivo:
    leitor = csv.DictReader(arquivo)
    total_salarios = 0
    for linha in leitor:
        total_salarios += float(linha["Salario"])