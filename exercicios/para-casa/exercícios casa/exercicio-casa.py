# Crie uma classe base chamada Veiculo com os seguintes atributos:
# - modelo: o modelo do veículo (uma string).
# - ano: o ano de fabricação do veículo (um número inteiro).
# - preco: o preço do veículo (um número decimal).

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


# criando a classe veiculo
class Veiculo:
    # definindo seus atributos
    def __init__(self, modelo, ano, preco):
        self.modelo = modelo
        self.ano = ano
        self.preco = preco

    # criando o método para calculo imposto que corresponde a 10% sobre o preço do veículo
    def calcular_imposto(self):
        return self.preco * 0.10

# criando a classe carro que herda atributos da classe veiculo
class Carro(Veiculo):
    def __init__(self, modelo, ano, preco, marca):
        super().__init__(modelo, ano, preco)
        self.marca = marca

# criando método para aplicar desconto de 5% sobre o valor do carro
    def calcular_desconto_carro(self):
        return self.preco * 0.05

# criando a classe moto que herda atributos da classe veiculo
class Moto(Veiculo):
    def __init__(self, modelo, ano, preco, cilindrada):
        super().__init__(modelo, ano, preco)
        self.cilindrada = cilindrada

    # criando o método para calculo imposto que corresponde a 5% sobre o preço da moto
    def calcular_imposto_moto(self):
        return self.preco * 0.05


carro = Carro("C4 Cactus", 2023, 106990.00, "Citroën")
moto = Moto("X-ADV", 2023, 91780.00, 745)


imposto_carro = carro.calcular_imposto()
print(f"\nO imposto a ser pago pelo carro {carro.modelo}, marca {carro.marca}, é de R$ {imposto_carro:.2f}.\n")

desconto_carro = carro.calcular_desconto_carro()
print(f"O desconto aplicado no carro {carro.modelo}, marca {carro.marca}, é de R$ {desconto_carro:.2f}.\n")

imposto_moto = moto.calcular_imposto_moto()
print(f"O imposto a ser pago pela moto modelo {moto.modelo}, que possui {moto.cilindrada}cc, é de R$ {imposto_moto:.2f}.\n")