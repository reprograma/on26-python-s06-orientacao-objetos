""

class retangulo:
    def __init__(self, base, altura):
       self.base = base
       self.altura = altura

    def calcular_area(self):
        area = self.base * self.altura
        return area
        

    def calcular_perimetro(self):
        perimetro = 2*(self.base + self.altura)
        return perimetro
      

retangulo1 = retangulo(int(input("Digite o comprimento da base do retângulo: ",)),int(input("Digite o comprimento da altura do retângulo: ",)))

area = retangulo1.calcular_area()
perimetro = retangulo1.calcular_perimetro()

print(f"Área do retângulo é de : {area} unidade(s) quadrada.")
print(f"O Perímetro do retângulo é de; {perimetro} u.c.")  