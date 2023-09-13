
class Retangulo:
    
    def __init__(self, altura, largura):
       # self.area = area
        #self.perimetro = perimetro
        self.altura = altura
        self.largura = largura
    
    def calcular_area( self):
        #  ou pode usar o self.area = self.altura * self.largura
        return self.altura*self.largura
        print(f' a area do retangulo é =  {self.area }')
       

        
    def calcular_perimetro( self):
       #  ou pode usar o  self.perimetro = 2* (self.altura + self.largura)
        return 2* self.altura+self.largura
        print(f' o valor do perimetro  é =  { self.perimetro}')
     

casa_carol = Retangulo (12.6, 14.5)      

casa_carol.calcular_area()
print(f' A casa da carol, tem {casa_carol.calcular_area() }  de area ')
casa_carol.calcular_perimetro()
print(f' A casa da carol, tem {casa_carol.calcular_perimetro() }  de perimetro ')


casa_largata = Retangulo(2, 3)
casa_largata.calcular_area
print(f' A casa da largata, tem {casa_largata.calcular_area() }  de area ')
casa_largata.calcular_perimetro
print(f' A casa da largata, tem {casa_largata.calcular_perimetro() }  de perimetro ')


         
             
    
    