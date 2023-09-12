'''
Crie uma classe chamada Retangulo para representar retângulos. 
Cada retângulo tem largura e altura. 
A classe deve incluir métodos para calcular a área e o perímetro.

Instruções:

Crie uma classe chamada Retangulo com os seguintes atributos:

largura: a largura do retângulo (um número decimal).
altura: a altura do retângulo (um número decimal).
Implemente os seguintes métodos na classe Retangulo:
'''

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura
#        print(f"O valor da área do retângulo é: {area}")
    
    def calcular_perimetro(self):
        return (2 * self.largura) + (2 * self.altura)
#        print(f"O valor da perímetro do retângulo é: {perimetro}")


dimensoes = Retangulo(10, 10)
print(f"\nA área do retângulo é: {dimensoes.calcular_area()}")
print(f"\nO perímetro do retângulo é: {dimensoes.calcular_perimetro()}")
print(f"\nA largura do retângulo é: {dimensoes.largura}\n")