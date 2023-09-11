'''Implemente o método calcular_aluguel() em cada uma das subclasses para calcular o valor do aluguel com base em regras específicas:
Para Casa, o aluguel deve ser calculado como preco_base + (area_terreno * 5).
Para Apartamento, o aluguel deve ser calculado como preco_base + (numero_quartos * 300).
e superclass tem o atributo endereco e nome_do_proprietario'''

#Calcular_aluguel
#Casa
#Apartamento
#area_terreno
#preco_base
#numero_de_quartos
#endereco
#Proprientario 

class Imovel:
    def __init__(self, proprietario, endereco, preco_base):
        self.proprietario = proprietario
        self.endereco = endereco
        self.preco_base = preco_base

    def calcular_aluguel(self):
        return self.preco_base
        
class Casa(Imovel):
    def __init__(self, proprietario, endereco, preco_base, area_terreno):
        super().__init__(proprietario, endereco, preco_base)
        self.area_terreno = area_terreno
    def aluguel_casa(self):
        return self.preco_base + (self.area_terreno * 5)   

class Apartamento(Imovel):
    def __init__(self, proprietario, endereco, preco_base, numero_de_quatos):
        super().__init__(proprietario, endereco, preco_base)
        self.numero_de_quartos = numero_de_quatos
    def aluguel_apto(self):
        return self.preco_base + (self.numero_de_quartos * 300)    

    
casa_dani = Casa('Braz', 'Rua Glicério Tavares 275,', 900, 120)

print(casa_dani.aluguel_casa())

apto_gabi = Apartamento('Braz', 'Rua Glicério Tavares, 275', 500, 4)

print(apto_gabi.aluguel_apto())