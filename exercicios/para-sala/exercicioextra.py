'''Exercicio extra
Implemente o método calcula_aluguel


'''

class Imovel:
    def __init__(self, endereco, nome_proprietario, preco_base):
        self.endereco = endereco
        self.nome_proprietario = nome_proprietario
        self.preco_base = preco_base

    def calcular_aluguel(self):
        return self.preco_base
    
class Casa(Imovel):
    def __init__(self, endereco, nome_proprietario, preco_base, area_terreno):
        super().__init__(endereco, nome_proprietario, preco_base)
        self.area_terreno = area_terreno

    def calcular_aluguel(self):
        resp = self.preco_base + (self.area_terreno * 5)
        return resp
    
class Apartamento(Imovel):
    def __init__(self, endereco, nome_proprietario, preco_base, num_quartos):
        super().__init__(endereco, nome_proprietario, preco_base)
        self.num_quartos = num_quartos

    def calcular_aluguel(self):
        resp = self.preco_base + (sel.num_quartos * 300)
        return resp
    
casa_jessica = Casa('122 Rua das Flores', 'Jessica Machado', 1500, 300)
apartamento_carlos = Apartamento('333, Av. Joao Mendes', 'Carlos Jose', 1200, 2)

print(casa_jessica.calcular_aluguel())