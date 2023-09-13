
class cachorro:
    def  __init__ ( self, nome,raca ): #init metodo construtor
        self.nome = nome
        self.raca = raca
        
    def andar (self):
        print( 'estou andando', self.nome)
    
    def info(self):
        print( self.nome, self.raca)
              

cachorro_lulu = cachorro( 'lulu', 'Hammier')
cachorro_rex = cachorro('rex','Pinscher')        

print(cachorro_lulu.info())

               
cachorro_lulu.info() 
cachorro_rex.info()

cachorro_lulu.andar() # depois do ponto é o metodo
cachorro_rex.andar()


"""A POO divide em 4 pilares:
Abstração
Encapsulamento
Herança
Polimorfismo
        """

