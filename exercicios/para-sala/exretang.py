#retangulo = retangulo(5.0, 3.0)
#perimetro = retangulo.calcular_perimetro()

class Retangulo:
    def __init__(self, largura, altura): # metodo construtor
        self.largura = input(float(largura))
        self.altura = input(float(altura))

    def calcular_area(self, area):
        area = (self.largura * self.altura)/2
        if self.largura != 0 and self.altura != 0:
            print(f'A área do triângulo informado é de {area}:.1f')
        else:
            print(f'Os valores informados são inválidos, tente novamente.')

    def calcular_perimetro(self, largura, perimetro):
        if self.largura != 0 and self.altura != 0:
            perimetro = (self.largura + self.altura)*2
            print(f'O perimetro do triângulo informado é de {perimetro}:.1f')
        else:
            print(f'Os valores informados são inválidos, tente novamente.')

