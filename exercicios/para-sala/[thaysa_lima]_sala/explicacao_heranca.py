class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        pass #serve para quando não queremos colocar nada no código, para não dar erro.

class Cachorro(Animal):
    def fazer_som(self):
        return (f"{self.nome} faz um latido")
    
class Gato(Animal):
    def fazer_som(self):
        return (f"{self.nome} faz um miado")

#super classe é a class Animal = mãe
#subclasse é o class Cachorro(Animal) = filha

class Pessoa:
    def __init__(self, nacionalidade, genero, nome, idade):
        self.nacionalidade = nacionalidade
        self.genero = genero
        self.nome = nome
        self.idade = idade

    def info(self): 
        print(self.nacionalidade, self.genero, self.nome, self.idade)

class PessoaProfissional(Pessoa):
    def __init__(self, nacionalidade, genero, nome, idade, setor, nivel ):
        super().__init__(nacionalidade, genero, nome, idade)
        #super serve para "chamar o que esta lá em cima, exemplo nesse caso ele irá pegar def __init__(self, nacionalidade, genero, nome, idade):
        # self.nacionalidade = nacionalidade
        # self.genero = genero
        # self.nome = nome
        # self.idade = idade"
        #agora continuamos os que faltam dentro do parenteses que são setor e nivel
        self.setor = setor
        self.nivel = nivel

    def info(self):
        super().info()
        print("Setor: ", self.setor)
        print("Nível: ", self.nivel)


maria_dba = PessoaProfissional("Brasileira", "Femenina", "Maria", "19", "Data", "Junior")

maria_dba.info()
