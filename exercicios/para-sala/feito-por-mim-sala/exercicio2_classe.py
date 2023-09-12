# - Exercício 2: Exercício de Classe, Atributo e Método (Nível Básico): Retângulo

# Crie uma classe chamada Retangulo para representar retângulos. Cada retângulo tem largura e altura. A classe deve incluir métodos para calcular a área e o perímetro do retângulo.

#nome da classe: retangulos
#atributos: largura e altura
#métodos: calcular área e calcular perímetro

class Retangulos: 
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return float((self.largura * self.altura))
    
    def calcular_perimetro(self):
        return (float((self.largura + self.altura) * 2))

#variável nova para aplicar a "formula" do retangulos, se eu quisr 
retangulo1 = Retangulos((float(input("Coloque aqui o valor da largura: "))), (float(input("Coloque aqui o valor da altura: "))))

print(f"Largura: {retangulo1.largura}")
print(f"Altura: {retangulo1.altura}")

area_retangulo1 = retangulo1.calcular_area()
perimetro_retangulo1 = retangulo1.calcular_perimetro()


print(f"Área: {area_retangulo1}")
print(f"Perímetro: {perimetro_retangulo1}")