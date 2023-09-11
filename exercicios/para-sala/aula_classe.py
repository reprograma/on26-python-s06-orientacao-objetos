class cachorro:
    def __init__(self, nome, raca): #Método construtor
        self.nome = nome
        self.raca = raca



    def andar (self):
        print('Estou andando', self.nome)

    def info(self):
        print(self.nome, self.raca)



cachorro_lulu = cachorro('lulu', 'harrier')

cachorro_rex = cachorro('rex', 'pinscher') 

print(cachorro_lulu.info())

cachorro_lulu.info()

cachorro_rex.info()

cachorro_lulu.andar()


b = - 1.8
a = 2


print(b.__class__)
