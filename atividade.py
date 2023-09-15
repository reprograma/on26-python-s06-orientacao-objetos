class Veiculo:
    def __init__(self, modelo, ano, preco):
        self.modelo = modelo
        self.ano = ano
        self.preco = preco

    def calcular_imposto(self):
        return 0.10 * self.preco

class Carro(Veiculo):
    def __init__(self, modelo, ano, preco, marca):
        super().__init__(modelo, ano, preco)
        self.marca = marca

    def desconto(self):
        return 0.05 * self.preco

class Moto(Veiculo):
    def __init__(self, modelo, ano, preco, cilindrada):
        super().__init__(modelo, ano, preco)
        self.cilindrada = cilindrada

    def calcular_imposto(self):
        return 0.05 * self.preco

carro_sofia = Carro('Mini Cooper', 2022, 30000.0, 'Mini')
moto_lorena = Moto('Harley Davidson', 2021, 15000.0, 250)

print(f'imposto do carro: R${carro_sofia.calcular_imposto()}')
print(f'imposto da moto: R${moto_lorena.calcular_imposto()}')
