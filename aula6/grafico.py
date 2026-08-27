import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. COLETA

df = pd.read_csv("vendas.csv",
                          sep=",", 
                          encoding="utf-8",
                          decimal=",",  
                          parse_dates=["data"])

df["valor"] = df["valor"].astype(float)
df["data"] = pd.to_datetime(df["data"])

# 2. LIMPEZA

print("Valores ausentes por coluna: ")
print(df.isnull().sum())

df = df.drop_duplicates()
df = df.dropna(subset=["data"])

# 3. EXPLORAR

print(f"\nTotal de registros válidos : {len(df)}")
print(df.describe())

# 4. ANÁLISE
resumo_vendedor = df.groupby("vendedor").agg(
    total_vendido = ("valor", "sum"),
    qnt_vendas = ("valor", "count"),
    media = ("valor", "mean"),
    mediana = ("valor", "median"),
).sort_values("total_vendido", ascending=False)

print(f"\nDesempenho")
print(resumo_vendedor)

print(f"Melhor vendedor: {resumo_vendedor.index[0]}")

# 5. VISUALIZAÇÃO

sns.set_style("whitegrid")

fig, ax = plt.subplots(figsize=(8,5))

sns.barplot(x=resumo_vendedor.index, y=resumo_vendedor["total_vendido"], ax=ax)
ax.set_title("Total vendido por vendedor")
ax.set_xlabel("Vendedor")
ax.set_ylabel("Total")

plt.tight_layout()
plt.savefig("resumo_vendedor.png")
plt.show()