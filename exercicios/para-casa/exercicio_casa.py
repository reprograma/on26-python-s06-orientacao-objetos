class Veiculo:
    def __init__(self, modelo, ano, preco):
        self.modelo = str(modelo)
        self.ano = int(ano)
        self.preco = float(preco)

    def calcular_imposto(self):
        imposto = 0.10 * self.preco
        return imposto
    
class Carro(Veiculo):
    def __init__(self, modelo, ano, preco, marca):
        super().__init__(modelo, ano, preco)
        self.marca = str(marca)

    def desconto(self):
        pre = 0.05 * self.preco
        return pre
    
class Moto(Veiculo):
    def __init__(self, modelo, ano, preco, cilindrada):
        super().__init__(modelo, ano, preco)
        self.cilindrada = int(cilindrada)

    def calcular_imposto(self):
        imposto = 0.05 * self.preco
        return imposto

meuCarro = Carro('Celta', 2013, 25.000, 'fiat')

print(meuCarro.calcular_imposto())

print(meuCarro.desconto())