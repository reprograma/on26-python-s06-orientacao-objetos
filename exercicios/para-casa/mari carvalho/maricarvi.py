class Veiculo:
    def __init__(self, modelo, ano, preco):
        self.modelo = modelo
        self.ano = ano
        self.preco = preco

    def calcular_imposto_carro(self):
        imposto = self.preco * 0.1
        return imposto
    
class Carro (Veiculo):
    def __init__(self, modelo, ano, preco, marca):
        super().__init__(modelo, ano, preco)
        self.marca = marca
    
    def calcular_desconto(self):
        desconto = self.preco * 0.05
        return desconto

class Moto (Veiculo):
    def __init__(self, modelo, ano, preco, cilindrada):
        super().__init__(modelo, ano, preco)
        self.cilindrada = cilindrada

    def calcular_imposto_moto(self):
        imposto = self.preco * 0.05
        return imposto

carro_andreza = Carro('esportivo', 2023, 25, 'porsche taycan')
moto_marcinha = Moto('custom', 2023, 60, 500)

print(carro_andreza.calcular_imposto_carro())
print(moto_marcinha.calcular_imposto_moto())

#Feito em chamada com as meninas da turma: 
# Andreza, Igea, Louise, Thaysa, Julia, Maria de Fatima, Marcinha