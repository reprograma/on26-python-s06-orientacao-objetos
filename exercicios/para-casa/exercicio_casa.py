class Veiculo:
    def __init__(self, modelo, ano, preco):
        self.modelo = modelo
        self.ano = ano
        self.preco = preco

    def calcular_imposto(self):
        super().__init__()
        imposto = self.preco * 0,10

    def descricao (self):
        return f'Modelo: {self.modelo}, Ano: {self.ano}, Preço: {self.preco}, Imposto: '
    
class Carro(Veiculo):
    def __init__(self, modelo, ano, preco, marca):
        super().__init__(modelo, ano, preco)
        self.marca = marca

    def desconto(self, valor):
        valor = self.preco *(5 / 100)
        return 
    

