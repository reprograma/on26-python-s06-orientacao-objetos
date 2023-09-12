"""Criando objeto no Python"""

class cachorro:
    def __init__(self, nome, raca):
        self.nome = nome
        self.raca = raca

    def andar(self):
        print("estou andando")

    def info(self):
        print(self.nome, self.raca)


cachorro_lulu = cachorro('lulu', 'Harrier')
cachorro_rex = cachorro('rex', 'Pinscher')

cachorro_lulu.info()
cachorro_rex.info()

cachorro_lulu.andar()


