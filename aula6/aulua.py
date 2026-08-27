import pandas as pd

tabela = pd.read_csv(
    "vendas.csv",
    sep=",",
    encoding="utf=8",
    decimal=",",
    parse_dates=["data"]
    )
"""
print(tabela.head())#5 linhas
print(tabela.shape)#linhas,colunas
print(tabela.columns.tolist())#tipos 
print(tabela.info())
print(tabela.describe())
print(tabela["vendedor"].unique())
print(tabela["produto"].value_counts())
"""
#print(tabela.isnull().sum())

tabela_sem_nulos = tabela.dropna()#geral
tabela_sem_nulos = tabela.dropna(subset=["produto"])#especificado
print(tabela_sem_nulos)


