#  Crie uma classe base chamada Veiculo com os seguintes atributos:
# modelo: o modelo do veículo (uma string).
# ano: o ano de fabricação do veículo (um número inteiro). preco: o preço do veículo 
# (um número decimal). Na classe Veiculo, implemente um método chamado calcular_imposto()
#  que retorna o imposto a ser pago pelo veículo. O imposto é calculado como 10% do preço do
#   veículo.Crie uma classe chamada Carro que herda da classe Veiculo. 
#   Adicione um atributo adicional:

# marca: a marca do carro (uma string). Na classe Carro, implemente um método chamado desconto() que retorna um desconto de 5% no preço do carro.
# Crie uma classe chamada Moto que também herda da classe Veiculo. Adicione um atributo adicional:

# cilindrada: a cilindrada da moto (um número inteiro). Na classe Moto, implemente um método chamado calcular_imposto() que calcula o imposto a ser pago pela moto. O imposto para motos é de 5% do preço do veículo.
# Crie instâncias de Carro e Moto, atribuindo valores adequados aos atributos de cada veículo.

# Calcule e imprima o imposto a ser pago por cada veículo usando o método calcular_imposto().

class Veiculo:
    def __init__(self, modelo, ano, preco):
        self.modelo = modelo
        self.ano = ano
        self.preco = preco

    def calcular_imposto(self):
        return 0.1 * self.preco  

class Carro(Veiculo):
    def __init__(self, modelo, ano, preco, marca):
        super().__init__(modelo, ano, preco)
        self.marca = marca

    def calcular_desconto(self):
        return self.preco  * 0.05 

class Moto(Veiculo):
    def __init__(self, modelo, ano, preco, cilindrada):
        super().__init__(modelo, ano, preco)
        self.cilindrada = cilindrada

    def calcular_imposto(self):
        return self.preco * 0.05 

carro1 = Carro("mini cooper", 2023, 25000.0, "BMW")
moto1 = Moto("Kawasaki Ninja", 2023, 15000.0, 1000)

imposto_carro1 = carro1.calcular_imposto()
print(f"Imposto a ser pago pelo carro {carro1.marca} {carro1.modelo}: R$ {imposto_carro1:.2f}")


desconto_carro1 = carro1.calcular_desconto()
print(f"Desconto aplicado no carro {carro1.marca} {carro1.modelo}: R$ {desconto_carro1:.2f}")


imposto_moto1 = moto1.calcular_imposto()
print(f"Imposto a ser pago pela moto (cilindrada {moto1.cilindrada}cc): R$ {imposto_moto1:.2f}")






#Feito em chamada com as meninas da turma: Andreza, Igea, Louise, Thaysa, Julia, Maria de Fatima, Marcinha