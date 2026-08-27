"""class Retangulo:
    def __init__(self,largura,altura):

        self.largura = largura
        self.altura = altura

    def area_retangulo(self):
        return self.largura * self.altura
    def perimetro_retangulo(self):
        return 2 * (self.largura + self.altura)

retangulo_1 = Retangulo(4,3)

retangulo_2 = Retangulo(5,5)

print(retangulo_1.area_retangulo())
print(retangulo_2.perimetro_retangulo())"""

"""
class ContaBancaria:

    def __init__(self,saldo_inicial = 0):

        self.saldo_inicial = saldo_inicial

    def depositar(self,valor_depositado):
        self.saldo_inicial += valor_depositado
        return self.saldo_inicial

    def sacar(self,valor_sacar):
        if valor_sacar > self.saldo_inicial:
            raise ValueError("Você não possue essa quantidade")
        valor_sacar -= self.saldo_inicial
        return self.saldo_inicial

conta_joao = ContaBancaria(100)

print(conta_joao.saldo_inicial)
print(conta_joao.depositar(200))
print(conta_joao.sacar(500))"""

""""
class Pessoa:

    def __init__(self,nome,cpf):
        self.nome = nome
        self.cpf = cpf

    def introducao(self):
        return (f"Olá, meu nome é {self.nome}")

class Funcionario(Pessoa):

    def __init__(self, nome, cpf,cargo):
        super().__init__(nome, cpf)
        self.cargo = cargo

    

funcionario = Funcionario("Pedro","089.831.111-00","Desenvolvedor")

print(funcionario.introducao())"""


class Animal:
    def __init__(self):
          return 

    def fazer_som(self):
        return None

class Cachorro (Animal):
    def __init__(self):
        super().__init__()

    def fazer_som(self):
        return ("Au Au")

class Gato (Animal):
    def __init__(self):
        super().__init__()

    def fazer_som(self):
        return ("Miau")

cachorro = Cachorro()
gato = Gato()

print(cachorro.fazer_som())
print(gato.fazer_som())
    
