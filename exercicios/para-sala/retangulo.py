class retangulo:
    def __init__ (self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    def areaRetangulo (self, largura, altura):
        areaRetangulo = (largura * altura)
        print("Área do retângulo: {areaRetangulo}")

    def perimetroRetangulo (self, largura, altura):
        perimetroRetangulo =  (2 * (largura + altura))
        print("Perímetro do retângulo: {perimetroRetangulo}")

retangulo.areaRetangulo(5,3)
retangulo.perimetroRetangulo(5,3)