# Classe Veículo com modelo, ano e preço. Calcular imposto de 10% do preço

class Veículo:
    def __init__(self, modelo, ano, preco):
        self.modelo = modelo
        self.ano = ano
        self.preco = preco

    def calcular_imposto(self):
        calculo = self.preco * 0.1
        return calculo
    
class Carro(Veículo):
    def __init__(self, modelo, ano, preco, marca):
        super().__init__(modelo, ano, preco)
        self.marca = marca

    def desconto(self):
        calculo_desconto = (self.preco * 0.05) # calculando o desconto do valor total
        imposto_com_desconto = (self.preco - calculo_desconto) * 0.1 # calculando o imposto considerando o desconto
        return imposto_com_desconto

class Moto(Veículo):
     def __init__(self, modelo, ano, preco, cilindrada):
        super().__init__(modelo, ano, preco)
        self.cilindrada = cilindrada

     def calcular_imposto(self):
        calculo = self.preco * 0.05
        return calculo
     
carro = Carro("hb20", 2023, 30000.0, "hyundai")
moto = Moto("pcx", 2023, 28000.0, 2000)

print(f"o imposto do carro a ser pago considerando o desconto é: R${carro.desconto()}")
print(f"o imposto do carro seria de R${carro.calcular_imposto()}, caso não houvesse desconto")
print(f"o imposto da moto é: R${moto.calcular_imposto()}")