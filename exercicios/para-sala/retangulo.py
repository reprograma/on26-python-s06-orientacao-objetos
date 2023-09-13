class retangulo:
    def _init_(self, largura, altura):
        self.largura= largura
        self.altura= altura

    def calcular_area(self):
        return self.altura*self.largura
    def calcular_perimetro(self):
        return 2*(self.altura+self.largura)
    
casa_teste = retangulo(1.0, 2.0)
print(f'A casa teste tem {casa_teste.calcular_area()} m^2')
print(f'a casa teste tem {casa_teste.calcular_perimetro()}')