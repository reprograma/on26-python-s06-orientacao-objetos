class cachorro:
    def init(self, nome, raca): # metodo construtor
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

b = 1
a = 2

print(b.__class__)

resp = b.__add__(a)

print(resp)