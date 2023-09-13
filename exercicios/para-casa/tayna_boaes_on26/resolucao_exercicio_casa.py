#Resolução Exercício de Casa

class Veiculo:
    def __init__(self, modelo, ano, preco):
        self.modelo = modelo
        self.ano = ano
        self.preco = preco
    
    def descricao(self):
        return f'\nModelo: {self.modelo}, Ano: {self.ano}, Preço R$:{self.preco}\n'
    
    def calcular_imposto(self):
        return self.preco
    
class Carro(Veiculo):
    def __init__(self,modelo, ano, preco, marca):
        super().__init__(modelo, ano, preco)
        self.marca = marca 
    
    def calcular_imposto (self):
        imposto_veiculo = self.preco + (self.preco * 10 / 100) - 5 / 100
        return imposto_veiculo

class Moto (Veiculo):
    def __init__(self, modelo, ano, preco, cilindrada):
        super().__init__(modelo, ano, preco)
        self.cilindrada = cilindrada
    def descricao(self):
        return f'\nModelo: {self.modelo}, Ano: {self.ano}, Preço R$:{self.preco}, Cilindrada: {self.cilindrada}\n'
    
    def calcular_imposto(self):
        imposto_moto = self.preco + (self.preco * 5 / 100)
        return imposto_moto
    

    
carro_tayna = Carro('Onix', 2023, 60.00 ,'Chevrolet')

print (carro_tayna.descricao())
print(carro_tayna.calcular_imposto())

moto_tayna = Moto('Street', 2022, 30.00, 250)
print(moto_tayna.descricao())
print(moto_tayna.calcular_imposto)