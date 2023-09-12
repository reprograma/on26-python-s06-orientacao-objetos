#exercicio para casa

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
    
#criacao de instâncias de Carro e Moto
carro = Carro('Fiat uno', 2020, 25000.00,'Fiat')
moto = Moto('Honda CBR300', 2021, 1500.00, 300)

#Cálculo e impressão do imposoto a ser pago
imposto_carro = carro.calcular_imposto()
desconto_carro = carro.desconto()
imposto_moto = moto.calcular_imposto()

print(f'Carro - Modelo : {carro.modelo}, Marca : {carro.marca}, Ano {carro.ano}\n')
print(f'Imposto a ser pago pelo carro : R$ {desconto_carro:.2f}\n')
print(f'Desconto no preco do carro: R$ {desconto_carro:.2f}\n')

print(f'Moto - Modelo: {moto.modelo}, Cilindrada : {moto.cilindrada}, Ano:{moto.ano}\n')
print(f'Imposto a ser pago pela moto : R$ {imposto_moto: .2f}')