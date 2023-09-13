# exercicio 2

class retangulo:
    def __init__ (self, altura, largura):
        self.altura = altura
        self.largura = largura
    
    def area (self, altura, largura):
        area_calculada = (altura * largura)
        return area_calculada
        print(area_calculada)

    def perimetro(self, altura, largura):
        perimetro_calculado = (altura) + (largura)
        return perimetro_calculado
        print(perimetro_calculado)

retangulo_mari = retangulo(8.0, 4.0)
print(retangulo_mari.area())
print(retangulo_mari.perimetro())

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        
    def calcular_area(self):
        # print(f'calcular a área{self.largura * self.altura}')
        return self.largura * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.largura + self.altura)
    
    
casa_fabiana = Retangulo(5.0, 3.0)

print(f'A casa da Fabiana, tem: {casa_fabiana.calcular_area()} área')

print(f'a casa da fabiana tem {casa_fabiana.calcular_perimetro()} de perímetro')
    


casa_daviny = Retangulo(9.0, 10.5)

print(casa_daviny.calcular_area())
print(casa_daviny.calcular_perimetro())


       