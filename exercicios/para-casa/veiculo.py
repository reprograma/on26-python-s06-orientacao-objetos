class veículo:
    def __init__(self, modelo, ano, valor):
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def calcular_imposto(self):
        calculo = self.valor * 0.1
        return calculo

class automovel(veículo):
    def __init__(self, modelo, ano, valor, marca):
        super().__init__(modelo, ano, valor)
        self.marca = marca

    def desconto(self):
        calculo_desconto = (self.valor * 0.05)
        imposto_com_desconto = (self.valor - calculo_desconto) * 0.1
        return imposto_com_desconto

class Moto(Veículo):
     def __init__(self, modelo, ano, valor, cilindrada):
        super().__init__(modelo, ano, valor)
        self.cilindrada = cilindrada

     def calcular_imposto(self):
        calculo = self.valor * 0.05
        return calculo

carro = carro("Uno", 2021, 69000.00, "Fiat")
moto = moto("BRW", 2023, 35000.00, "Honda")

print(f"o imposto do carro com o desconto é: R$ {carro.desconto()}")
print(f"o imposto do carro será de R$ {carro.calcular_imposto()}, caso não ocorrer desconto")
print(f"o imposto da moto é: R$ {moto.calcular_imposto()}")