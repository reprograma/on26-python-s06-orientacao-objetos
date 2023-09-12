#exercicio principal
class Veiculo:
    def __init__(self, modelo, ano, preco):
        self.modelo = modelo
        self.ano = ano
        self.preco = preco
        
    def calcular_imposto(self):
        imposto =  self.preco * 0.10
        return imposto
    
class Carro(Veiculo):
    def __init__(self, modelo, ano, preco, marca):
        super().__init__(modelo, ano, preco)
        self.marca = marca
        
    def desconto(self):
        desconto = self.preco - (self.preco * 0.05) 
        return desconto
    
    
class Moto(Veiculo):
    def __init__(self, modelo, ano, preco, cilindrada):
        super().__init__(modelo, ano, preco)
        self.cilindrada = cilindrada
        
    def calcular_imposto_moto(self):
        imposto = self.preco * 0.05
        return imposto
            
    
carro = Carro('Corolla', 2023, 500.000, 'Honda')

moto = Moto('CBR500R', 2022, 17.000, 120)


print(f" O valor do Carro com desconto de 5% ficou de R$: {carro.desconto()}")

print(f" O Valor do imposto a pagar da Moto  de 5% é R$: {moto.calcular_imposto_moto():.2}")

print (f" O imposto a pagar do Carro é de R$: {carro.calcular_imposto()}")

print (f" O imposto a pagar da Moto é de RS: {moto.calcular_imposto():.2}")
       

