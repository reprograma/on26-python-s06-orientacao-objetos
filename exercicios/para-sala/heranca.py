class animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        pass
    
class cachorro(animal):
    def fazer_som(self):
        return f'{self.nome} faz um latido'
    def andar(self):
        pass

class gato(animal):
    def fazer_som(self):
        return f'{self.nome} faz um miado'
    
class person:
    def __init__(self, nascionalidade, genero, nome, idade):
        self.nascionalidade = nascionalidade
        self.genero = genero
        self.nome = nome
        self.idade = idade

    def info(self):
        print(self.nascionalidade, self.genero, self.nome, self.idade)

class personprofessional(person):
    def __init__(self, nascionalidade, genero, nome, idade, setor, nivel):
        super().__init__(nascionalidade, genero, nome, idade)
        self.setor = setor
        self.nivel = nivel

    def info(self):
        super().info()
        print("setor: ", self.setor)
        print("nivel:", self.nivel)

maria_dba = personprofessional('brasileira', 'feminina', 'Maria', '19', 'data', 'junior')
maria_dba.info()
    