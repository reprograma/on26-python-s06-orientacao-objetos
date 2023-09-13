#Exercício 2: Animais
#Crie uma classe abstrata chamada Animal com métodos abstratos emitir_som() e mover().
#Em seguida, crie subclasses concretas como Cachorro, Gato e Pato que herdam da classe Animal.
#Cada uma das subclasses deve implementar os métodos emitir_som() e mover() de acordo com o comportamento apropriado para cada animal.

class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, num_portas):
        super().__init__(marca, modelo, ano):
        self.num_portas = num_portas

    def descricao(self):
        return super().descricao() + f',Numero de portas: {self.num_portas}'
    
class Motos(Veiculo)