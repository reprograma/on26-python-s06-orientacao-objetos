"""class Animal:
    def __init__(self, nome):
     self.nome = nome
     
    def fazer_som(self):
        pass
    
    
class Cachorro(Animal): # herda com a classe entre pareteses
    def fazer_som (self):
        return f'{ self.nome} faz latido'
    def andar(self)
    pass # quando não quizer colocar nada dentro uso pass
    
class Gato(Animal):
    def fazer_som (self):
        return f'{ self.nome} faz miado' 
    
animal_1 =  Animal( 'kaki')
cachorro_da_gabi  = Cachorro()
cachorro_da_gabi.fazer_som()
"""
#----


class Person:
    def __init__(self, nacionalidade, genero, nome, idade):
        self.nacionalidade = nacionalidade
        self.genero = genero
        self.nome = nome
        self.idade = idade
        
    def info(self):    
        print(self.nacionalidade, self.genero, self.nome, self.idade)
    
class PersonProfessional(Person):
    def __init__(self, nacionalidade,genero,nome,dade, setor, nivel ):
        super().__init__ (nacionalidade,genero,nome,dade)  
        self.setor = setor
        self.nivel = nivel
        
        
        
        
    def info(self):
        super().info()
        print("Setor:", self.setor)
        print("Nível:", self.nivel)
        
        
maria_dba = PersonProfessional('brasileira', 'feminina', 'Maria', '19', 'data', 'junior')

maria_dba.info()


