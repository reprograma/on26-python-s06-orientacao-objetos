# - Exercício 1: Veículos - Herança

# Crie um sistema de gerenciamento de veículos. Crie uma classe base chamada Veiculo com os seguintes atributos:
#     - marca: a marca do veículo.
#     - modelo: o modelo do veículo.
#     - ano: o ano de fabricação do veículo.
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
        return (f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}")
    
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, lugares):
        super().__init__(marca, modelo, ano)
        self.lugares = lugares

    def descricao(self):
        return f"Carro - {super().descricao()}, Ocupação no veículo: {self.lugares}"

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindros):
        super().__init__(marca, modelo, ano)
        self.cilindros = cilindros

    def descricao(self):
        return f"Moto - {super().descricao()}, Cilindradas: {self.cilindros}"
    
carro1 = Carro("Ford", "Fiesta", 2022, 4)
moto1 = Moto("Honda", "CBR500R", 2021, "1000")

print(carro1.descricao())  
print(moto1.descricao())   