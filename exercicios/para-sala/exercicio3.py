#- Exercício 3: Veículos

#Crie um sistema de gerenciamento de veículos. Crie uma classe base chamada Veiculo com os seguintes atributos:

 #   - marca: a marca do veículo.
 #  - modelo: o modelo do veículo.
 #  - ano: o ano de fabricação do veículo.

    
# A classe Veiculo deve ter um método chamado `descricao()` que retorna uma descrição completa do veículo.

# Crie duas subclasses concretas, Carro e Moto, que herdam da classe Veiculo. Adicione atributos específicos para cada tipo de veículo, como número de portas para carros e tipo de motor para motos.

# Implemente o método `descricao()` em cada uma das subclasses para incluir informações específicas do tipo de veículo.

# Crie instâncias de Carro e Moto, atribuindo valores adequados aos atributos de cada veículo. Use o método `descricao()` para exibir informações detalhadas sobre cada veículo.


class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        
    def descricao(self):
        return f'Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}'
    
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, num_portas):
        super().__init__(marca, modelo, ano)
        self.num_portas = num_portas
        
    def descricao(self):
        return super().descricao() + f', Números de portas: {self.num_portas}'
    
    
class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, tipo_motor):
        super().__init__(marca, modelo, ano)
        self.tipo_motor = tipo_motor
        
    def descricao(self):
        return super().descricao() + f'tipo de motor: {self.tipo_motor}'
    
    
carro = Carro('Toyota', 'Corolla', 2023, 4)

moto = Moto('honda', 'CBR500R', 2022, '4 tempos')


print(carro.descricao())

print(moto.descricao())


carro_joao = Carro('Fiat', 'Siena', 2018, 4)


print(carro_joao.descricao())