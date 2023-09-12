#implementar o método calcular_aluguel() em cada uma das subclasses para calcular o valor do aluguel
#para Casa (subclasse) o aluguel deve ser calculado como preco_base + (area_terreno*5)
#para Apartamento (subclasse) o aluguel deve ser calculado como preco_base + (numero_quartos*300)
#a superclasse tem atributo endereco e nome_do_proprietario

class Imovel:
    def __init__(self,endereco, nome_do_proprietario, preco_base):
        self.endereco = endereco
        self.nome_do_proprietario= nome_do_proprietario
        self.preco_base = preco_base
        
    def calcular_aluguel(self):
        return self.preco_base


class Casa(Imovel):
    def __init__(self, endereco, nome_do_proprietario, preco_base, area_terreno):
        super().__init__(endereco, nome_do_proprietario, preco_base)
        self.area_terreno = area_terreno
    
    def calcular_aluguel(self):
        return self.preco_base + (self.area_terreno * 5)

class Apartamento(Imovel):
    def __init__(self, endereco, nome_do_proprietario, preco_base, numero_quartos):
        super().__init__(endereco, nome_do_proprietario, preco_base)
        self.numero_quartos = numero_quartos

    def calcular_aluguel(self):
        return self.preco_base + (self.numero_quartos * 300)

                  
                 #endereço nome do proprietário/preco base/area do terreno   
casa_maria = Casa("122 Rua das Camélias", "Maria Lorena", 1200, 340)

apartamento_thaysa = Apartamento("333 Av. João Mendes", "Thaysa Lima", 1200, 2)

print(f"A casa da Maria será no valor de: {casa_maria.calcular_aluguel()}")
print(f"O apartamento da Thaysa será no valor de: {apartamento_thaysa.calcular_aluguel()}")
