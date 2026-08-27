class Produto:
    def __init__(self,nome,preco,quantidade = 0):
        if preco <= 0:
            raise ValueError("Preço deve ser positivo")
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def valor_em_estoque(self):
        return self.preco * self.quantidade

    def repor_estoque(self, qtd_adicional):
        if qtd_adicional <= 0:
            raise ValueError("Quantidade deve ser positiva")
        self.quantidade += qtd_adicional

notebook = Produto("Notebook Pro", 3500.00,10)
mouse = Produto("Mouse wireless",45.00,50)

print(notebook.nome,notebook.preco,notebook.quantidade)