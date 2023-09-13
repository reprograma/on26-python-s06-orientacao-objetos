"""
exercício extra
implemente o método calcular_aluguel() em cada uma das subclasses para calcular o valor do
aluguel com base em regras específicas:
Para Casa, o aluguel deve ser calculado como preco_base + (area_terreno * 5).
Para Apartamento, o aluguel deve ser calculado como preco_base + (numero_quartos * 300).
e superclass tem o atributo endereco e nome_do_proprietario
"""


class Imovel:
    
    def __init__(self, endereco, nome_proprietario, preco_base):
        self.endereco = endereco
        self.nome_proprietario = nome_proprietario
        self.preco_base = preco_base
        
        

    
    def calcular_aluguel(self):
          return self.preco_base

class Casa (Imovel):  
    def __init__(self, endereco, nome_proprietario, preco_base, area_terreno):
        super().__init__(endereco, nome_proprietario, preco_base)    
        self.area_terreno = area_terreno
        
    def calcular_aluguel(self):
        resp =  self.preco_base + (self.area_terreno * 5)
        return resp
         
class  Apartamento (Imovel):  
    def __init__(self, endereco, nome_proprietario, preco_base, num_quartos):
        super().__init__(endereco, nome_proprietario, preco_base)    
        self.num_quartos = num_quartos 

    def calcular_aluguel(self):
        resp =  self.preco_base + (self.numero_quartos * 300)
        return resp           
                
casa_maria = Casa("122 Rua das Flores", "Maria", 1500, 120)
apartamento_carlos = Apartamento("333, Av. João Mendes", 'Carlos Jose', 1200, 2)


print(casa_maria.calcular_aluguel())               