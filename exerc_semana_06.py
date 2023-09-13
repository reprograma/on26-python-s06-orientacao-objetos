# ## 👩🏻‍💻 Crie uma classe base chamada Veiculo com os seguintes atributos:

# - modelo: o modelo do veículo (uma string).
# - ano: o ano de fabricação do veículo (um número inteiro).
# preco: o preço do veículo (um número decimal).
# Na classe Veiculo, implemente um método chamado `calcular_imposto()` que retorna o imposto a ser pago pelo veículo. 

# O imposto é calculado como 10% do preço do veículo.

# Crie uma classe chamada Carro que herda da classe Veiculo. Adicione um atributo adicional:

# - marca: a marca do carro (uma string).
# Na classe Carro, implemente um método chamado desconto() que retorna um desconto de 5% no preço do carro.

# Crie uma classe chamada Moto que também herda da classe Veiculo. Adicione um atributo adicional:

# - cilindrada: a cilindrada da moto (um número inteiro).
# Na classe Moto, implemente um método chamado `calcular_imposto()` que calcula o imposto a ser pago pela moto. 

# O imposto para motos é de 5% do preço do veículo.

# Crie instâncias de Carro e Moto, atribuindo valores adequados aos atributos de cada veículo.

# Calcule e imprima o imposto a ser pago por cada veículo usando o método `calcular_imposto()`.

class Veiculo:
    def __init__(self, modelo, ano, preco, imposto): # IMPOSTO VAI AQUI??? ACHO QUE NAO NE?
        self.modelo = modelo
        self.ano = ano
        self.preco = preco
        self.imposto = imposto

    # def calcular_imposto(self):
    #     self.imposto = (self.preco)*0.90
    #     return self.imposto
    
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, preco, imposto):
        super().__init__(modelo, ano, preco, imposto)
        self.marca = marca

    # def desconto():
    #     return super().preco*0.95
        
class Moto(Veiculo):
    def __init__(self, modelo, cilindrada, ano, preco, imposto):
        super().__init__(modelo, ano, preco, imposto)
        self.cilindrada = cilindrada

# carro_da_lais = Carro("Chevrolet", "Corsa", 2009, 10, 0)
# print(carro_da_lais.desconto)