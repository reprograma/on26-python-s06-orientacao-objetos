class Animal:
    def __init__(self, nome):
        self.nome = nome
        
    def fazer_som(self):
        pass #é uma palavra reservada, usada quando não queira escrever nada

#a classe cachorro herda Animal, ela herda tanto o metodo como os atributos    
class Cachorro(Animal):
    def fazer_som(self):#metodo
        return (f'{self.nome} faz um latido')
    
    def andar(self):
       pass
    
class Gato(Animal):
    def fazer_som(self):
        return (f'{self.nome} faz um miado')

Animal_1 = Animal('kaki')

Animal_1.fazer_som()

#####

class Person:
    def __init__(self, nacionalidade, genero, nome, idade):
        self.nacionalidade = nacionalidade
        self.genero = genero
        self.nome = nome
        self.idade = idade
        
    def info(self):
        print(self.nacionalidade, self.genero, self.nome, self.idade)
        
class PersonProfessional(Person):
    def __init__(self, nacionalidade, genero, nome, idade, setor, nivel):
        super().__init__(nacionalidade, genero, nome, idade)
        self.setor = setor
        self.nivel = nivel
        
    def info(self):
        super().info()
        print("Setor :", self.setor)
        print("Nivel: ", self.nivel)
 
maria_dba = PersonProfessional('brasileira', 'feminina', 'Maria', '19', 'data', 'junior')

maria_dba.info()           
