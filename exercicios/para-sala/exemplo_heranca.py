class Animal:
    def __init__(self, nome): 
        self.nome = nome

    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        return f'{self.nome} faz um latido'

class Animal:
    def __init__(self, nome):
        self.nome = nome
        
    def fazer_som(self):
        pass
    
class Cachorro(Animal):
    def fazer_som(self):
       return f'{self.nome} faz um latido'
   
    def andar(self):
       pass
   

class Gato(Animal):
    def fazer_som(self):
        return f'{self.nome} faz um miado'

# ----

class Person:
    def __init__(self, nacionalidade, genero, nome, idade):
        self.nacionalidade = nacionalidade
        self.genero = genero
        self.nome = nome
        self.idade = idade
    
    def info(self):
        print(self.nacionalidade, self.genero, self.nome, self.idade)
        
class PersonProfessional(Person):
    def __init__ (self, nacionalidade, genero, nome, idade, setor, nivel):
        super().__init__(nacionalidade, genero, nome, idade)
        self.setor = setor
        self.nivel = nivel
        
        
    def info(self):
        super().info()
        print("Setor:", self.setor)
        print("Nível:", self.nivel)
        

maria_dba = PersonProfessional('brasileira', 'feminina', 'Maria', '19', 'data', 'junior')

maria_dba.info()





