class veiculo:
    def __init__(self, modelo, ano, preco):
        self.modelo = str(modelo)
        self.ano = int(ano)
        self.preco = float(preco)

    def calculaImposto(self):
        imp = 0.1 * self.preco
        return imp

class carro(veiculo):
    def __init__(self, modelo, ano, preco, marca):
        super().__init__(modelo, ano, preco)
        self.marca = str(marca)

    def desconto(self):
        preco = 0.95 * self.preco
        return preco

class moto(veiculo):
    def __init__(self, modelo, ano, preco, cilindrada):
        super().__init__(modelo, ano, preco)
        self.cilindrada = int(cilindrada)

    def calculaImposto(self):
        imp = 0.3 * self.preco
        return imp


veiculoJoana = moto('abc-1', 2008, 1200.00, 500)

print(veiculoJoana.calculaImposto()) 

veiculoDarla = carro('uno', 2006, 70000, 'fiat')

print(veiculoDarla.desconto())