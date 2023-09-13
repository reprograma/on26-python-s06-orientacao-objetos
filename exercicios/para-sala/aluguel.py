class Imovel:
    def __init__(self, endereco, proprietario, preco_base):
        self.endereco = endereco
        self.proprietario = proprietario
        self.preco_base = preco_base
        
    def calcular_aluguel(self):
            return self.preco_base
        
class Casa(Imovel):
    def __init__(self, endereco, proprietario, preco_base, area_terreno):
        super().__init__(endereco, proprietario, preco_base)
        self.area_terreno = area_terreno
        
    def calcular_aluguel(self):
        resp =  self.preco_base + (self.area_terreno * 5)
        return resp
    
class Apartamento(Imovel):
    def __init__(self, endereco, proprietario, preco_base, numero_quartos):
        super().__init__(endereco,proprietario, preco_base)
        self.numero_quartos = numero_quartos
        
    def calcular_aluguel(self):
        resp =  self.preco_base + (self.numero_quartos * 300)
        return resp
    
    
casa_francisca = Casa("Santo Anastácio, 940,", "Francisca", 1500, 300)
apartamento_carlos = Apartamento("Tamareiras, 967", 'Raimundo', 1200, 2)

print(casa_francisca.calcular_aluguel())
print(apartamento_carlos.calcular_aluguel())
