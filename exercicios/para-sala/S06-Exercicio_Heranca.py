'''
Crie uma classe base chamada Veiculo com os seguintes atributos:

- modelo: o modelo do veículo (uma string).
- ano: o ano de fabricação do veículo (um número inteiro).
- preco: o preço do veículo (um número decimal).
Na classe Veiculo, implemente um método chamado `calcular_imposto()` que retorna o imposto a ser pago pelo veículo. 
O imposto é calculado como 10% do preço do veículo.

Crie uma classe chamada Carro que herda da classe Veiculo. Adicione um atributo adicional:

- marca: a marca do carro (uma string).
Na classe Carro, implemente um método chamado desconto() que retorna um desconto de 5% no preço do carro.

Crie uma classe chamada Moto que também herda da classe Veiculo. Adicione um atributo adicional:

- cilindrada: a cilindrada da moto (um número inteiro).
Na classe Moto, implemente um método chamado `calcular_imposto()` que calcula o imposto a ser pago pela moto. 
O imposto para motos é de 5% do preço do veículo.

Crie instâncias de Carro e Moto, atribuindo valores adequados aos atributos de cada veículo.

Calcule e imprima o imposto a ser pago por cada veículo usando o método `calcular_imposto()`.
'''

class Veiculo:
    def __init__(self, modelo, ano, preco):
        self.modelo = modelo
        self.ano = ano
        self.preco = preco
    
    def calcular_imposto(self):
        imposto = self.preco * 0.1
        return f"\nO valor do imposto do veículo é R${imposto:.2f}\n"
    
class Carro(Veiculo):
    def __init__(self, modelo, ano, preco, marca):
        super().__init__(modelo, ano, preco)
        self.marca = marca
    
    def calcular_desconto(self):
        desconto = self.preco * 0.05
        return f"\nO preço do carro {self.modelo} do ano {self.ano} com desconto de 5% é R${(self.preco - desconto):.2f}"

class Moto(Veiculo):
    def __init__(self, modelo, ano, preco, cilindradas):
        super().__init__(modelo, ano, preco)
        self.cilindradas = cilindradas
    
    def calcular_imposto(self):
        imposto = self.preco * 0.05
        return f"\nO valor do imposto da moto {self.modelo} do ano {self.ano} é R${imposto:.2f}\n"

while True:

    veiculo = input("Qual o seu veículo, moto ou carro?\n").lower()

    if veiculo == "moto":
        modelo_moto = input("Qual o modelo da moto?\n")
        preco_moto = float(input("Qual o preço da moto?\n"))
        imposto_moto = Moto("Bis", 2012, 7000, 100)
        print(imposto_moto.calcular_imposto())
        break
    elif veiculo == "carro":
        modelo_carro = input("Qual o modelo do carro?\n")
        preco_carro = float(input("Qual o preço do carro?\n"))
        desconto_celta = Carro("Celta", 2014, preco_carro, "Chevrolet")
        print(desconto_celta.calcular_desconto())
        imposto_veiculo = Veiculo("Celta", 2014, 30000)
        print(imposto_veiculo.calcular_imposto())
        break
    else:
        print("Veículo deve ser Moto ou Carro. ")