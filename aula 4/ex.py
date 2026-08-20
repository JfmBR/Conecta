import csv

resumo_vendas = {}

with open("vendas.csv", "r",newline="", encoding="UTF=8") as file:
    leitor = csv.DictReader()
    for linha in leitor:
        categoria = linha["categoria"]
        valor = float(linha["valor"])
        resumo_vendas["categoria"] = resumo_vendas.get(categoria)

for categoria, total in sorted(resumo_vendas.items()):
    print(f"{}") 