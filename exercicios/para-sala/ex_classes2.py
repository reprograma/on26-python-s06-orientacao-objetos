class Retangulo:
    def __init__ (self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    def calcular_area (self):
        #print (f'calcular a área{self.largura * self.altura}')
        return self.largura * self.altura

    def calcular_perimetro (self):
        return 2 * (self.largura + self.altura)
    
casa_fabiana = Retangulo(5.0, 3.0)

print(f'A casa da Fabiana tem: {casa_fabiana.calcular_area()} area')

print(f'A casa da Fabiana tem: {casa_fabiana.calcular_perimetro()} de perimetro')




    