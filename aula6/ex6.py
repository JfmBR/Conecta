import pandas as pd

tabela = pd.read_csv(
    "vendas.csv",
    sep=",",
    encoding="utf=8",
    decimal=",",
    parse_dates=["data"]
    )

"""
nome = tabela["produto"]#serie
nomes = tabela[["produto","valor"]]#dataframe

print(nomes)

primeira_linha = tabela.iloc[0]
tres_primeiras = tabela.iloc[0:3]
produtos = ["Mouse","Notebook"]

filtrado = tabela[tabela["produto"].isin(produtos)]
print (filtrado)

total_vendedor = tabela.groupby("vendedor")["valor"].sum()

print(total_vendedor.sort_values(ascending=False))




resumo_geral = tabela.groupby("vendedor").agg(
    total = ("vendas","sum"),
    media = ("valor","mean"),
    quantidade_vendas = ("valor","count")
).reset_index()

"""
tabela["Caro"] = tabela["valor"].apply(
    lambda p: "caro" if p > 1000 else "normal"
)
