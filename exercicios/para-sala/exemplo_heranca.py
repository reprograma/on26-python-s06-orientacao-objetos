class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        return f"{self.nome} faz um latido."
    
class Gato(Animal):
    def fazer_som(self):
        return f"{self.nome} faz um miado."

#animal_1 = Animal("Kaki")
#cachorro_da_gabi = Cachorro()
#cachorro_da_gabi.fazer_som()

#----

class Person:
    def __init__(self, nacionalidade, genero, nome, idade):
        self.nacionalidade = nacionalidade
        self.genero = genero
        self.nome = nome
        self.idade = idade

    def info(self):
        print(self.nacionalidade, self.genero,self.nome, self.idade)

class PersonProfessional(Person):
    def __init__ (self, nacionalidade, genero, nome, idade, setor, nivel):
        super().__init__(nacionalidade, genero, nome, idade)
        self.setor = setor
        self.nivel = nivel

    def info(self):
        super().info()
        print("Setor: ", self.setor)
        print("Nível: ", self.nivel)

maria_dba = PersonProfessional("brasileira", "mulher cis", "Maria", "19", "data","junior")
maria_dba.info()

# ----

class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def descricao(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}"

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, num_portas):
        super().__init__(marca, modelo, ano)
        self.num_portas = num_portas
    
    def descricao(self):
        return super().descricao() + f", Número de portas: {self.num_portas}"

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, tipo_motor):
        super().__init__(marca, modelo, ano)
        self.tipo_motor = tipo_motor

    def descricao(self):
        return super().descricao() + f"tipo de motor: {self.tipo_motor}"

carro = Carro("Toyota", "Corolla", 2023, 4)

moto = Moto("Honda", "CBR500R", 2022, "4 tempos")

print(carro.descricao())

print(moto.descricao())

carro_joao = Carro("Fiat", "Siena", 2018, 4)

print(carro_joao.descricao())