# Exercício 2: Exercício de Classe, Atributo e Método (Nível Básico): Retângulo

# Crie uma classe chamada Retangulo para representar retângulos. Cada retângulo tem largura e altura. A classe deve incluir métodos para calcular a área e o perímetro do retângulo.

# Instruções:

# Crie uma classe chamada Retangulo com os seguintes atributos:

# largura: a largura do retângulo (um número decimal).
# altura: a altura do retângulo (um número decimal).
# Implemente os seguintes métodos na classe Retangulo:

# __init__(self, largura, altura): O construtor que inicializa os atributos da largura e altura.
# calcular_area(self): Um método que calcula a área do retângulo (área = largura * altura).
# calcular_perimetro(self): Um método que calcula o perímetro do retângulo (perímetro = 2 * (largura + altura)).
# Exemplo:

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


    
            