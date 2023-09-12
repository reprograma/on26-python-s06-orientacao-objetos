class animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        pass

class cachoro(animal):
    def fazer_som(self):
        return f'{self.nome} faz um latido'

class gato(animal):
    def fazer_som(self):
        return f'{self.nome} faz um miado'

animal_1 = animal('kaki')

cachoro_da_gabi = cachoro()

cachoro_da_gabi.fazer_som()


# ----

class person:
    def __init__(self, nacionalidade, genero, nome, idade):
        self.nacionalidade = nacionalidade
        self.genero = genero
        self.nome = nome
        self.idade = idade

    def info(self):
        print(self.nacionalidade, self.genero, self.nome, self.idade)

class personprofessional(person):
    def __init__(self, nacionalidade, genero, nome, idade, setor, nivel):
        super().__init__(nacionalidade, genero, nome, idade)
        self.setor = setor
        self.nivel = nivel

    def info(self):
        super().info()
        print("Setor:", self.setor)
        print("Nível:", self.nivel)

maria_dba = personprofessional ('brasileira', 'feminina', 'Maria', '19', 'data', 'junior')

maria_dba.info()