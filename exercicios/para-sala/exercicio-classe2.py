'''
Exercicio 2:
Crie uma classe chamada retangulo para representar retangulos. Cada retangulo tem largura e altura.
A classe deve incluir métodos para calcular a área e o perímetro do retangulo.
'''

class retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    def calcular_area(self):
        #print(f'calcular a area {self.largura * self.altura}')
        return self.largura *self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.largura + self.altura)

casa_fabiana = retangulo(5.0, 3.0)
print(f'A casa da Fabina tem {casa_fabiana.calcular_area()}m2 de área')
print(f'A casa da Fabiana tem {casa_fabiana.calcular_perimetro()}m de perimetro')

casa_jessica = retangulo(9.0, 10.5)

print(casa_jessica.calcular_area())
print(casa_jessica.calcular_perimetro())
print(casa_jessica.largura)
