# Exercicio 2 Retangulo

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        
    def calcular_area(self):
        # print(f'calcular a área{self.largura * self.altura}')
        return self.largura * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.largura + self.altura)
    
    
casa_fatima = Retangulo(5.0, 3.0)

print(f'A casa da Fatima, tem: {casa_fatima.calcular_area()} área')

print(f'a casa da fatima tem {casa_fatima.calcular_perimetro()} de perímetro')
    


casa_fatima = Retangulo(9.0, 10.5)

print(casa_fatima.calcular_area())
print(casa_fatima.calcular_perimetro())

print(f'a casa da Fatima, tem:{casa_fatima.calcular_area()} área')

print(f'a casa da Fatima tem {casa_fatima.calcular_perimetro()} de perímetro')
    


casa_fatima = Retangulo(9.0, 10.5)

print(casa_fatima.calcular_area())
print(casa_fatima.calcular_perimetro())