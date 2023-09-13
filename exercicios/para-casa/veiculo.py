

class veiculo:
    def __init__(self, modelo, anoFabricacao, preco):
        self.modelo = modelo
        self.anoFabricacao = anoFabricacao
        self.preco = preco

    def calcularImposto(self):
        imposto = (self.preco * 0.10)
        return imposto
    
class carro(veiculo):
    def __init__(self, modelo, anoFabricacao, preco, marca):
        super().__init__(modelo, anoFabricacao, preco)
        self.marca = marca

    def calcularImposto(self):
        imposto = (self.preco * 0.10)
        return imposto

    def daDesconto(self):
        desconto = (self.preco * 0.05)
        return desconto
    
class moto(veiculo):
    def __init__(self, modelo, anoFabricacao, preco, cilindrada):
        super().__init__(modelo, anoFabricacao, preco)
        self.cilindrada = cilindrada
    
    def calcularImposto(self):
        imposto = (self.preco * 0.05)
        return imposto

carro01 = ("iX3 M Sport", 2011, 500950, "BMW")
moto01 = ("Nightster™ Special", 2023, 111.900, 975)

impostoCarro = carro01.calcularImposto()
impostoMoto = moto01.calcularImposto()

print("Imposto total do {carro01.modelo}: R${impostoCarro}")
print("Imposto total da moto {moto01.modelo}: R${impostoMoto}")