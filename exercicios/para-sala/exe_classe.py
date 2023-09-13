
# class cachorro:
#     def __init__(self, nome, raca): #metodo construtor
#        self.nome = nome
#        self.raca = raca

#     def andar(self):
#      print("estou andando", self.nome)

#     def info(self):
#         print(self.nome, self.raca)

        
# cachorro_lulu = cachorro("lulu", "Harier")

# cachorro_rex = cachorro ("rex", "Pinscher")
    
    
    
# print(cachorro_lulu.info())

# cachorro_lulu.info()
# cachorro_rex.inf()
# cachorro_lulu.andar()    
class cachorro:
    def __init__(self, nome, raca): # metodo construtor
        self.nome = nome
        self.raca = raca
        
    def andar(self):
        print('estou andando', self.nome)
        
    def info(self):
        print(self.nome, self.raca)
           
        
cachorro_lulu = cachorro('lulu', 'Harrier')

cachorro_rex = cachorro('rex', 'Pinscher')

# .... N objetos
          
cachorro_lulu.info()

cachorro_rex.info()

cachorro_lulu.andar()

print(f'nome do meu cachoro: {cachorro_lulu.nome}')

cachorro_lulu.nome

cachorro_rex.andar()
