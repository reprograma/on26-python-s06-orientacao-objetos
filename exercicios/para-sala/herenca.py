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
    


animal_1 = cachorro('billy')

cachorro_da_dani = animal_1

acao_dog = cachorro_da_dani.fazer_som()

print(acao_dog)

# ....

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
        print("setor:", self.setor)  
        print("nivel:", self.nivel)


maria_dba = ('brasileira')