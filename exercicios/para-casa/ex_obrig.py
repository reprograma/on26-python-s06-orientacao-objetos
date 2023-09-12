# Crie uma classe base chamada Veiculo com os seguintes atributos:

#     modelo: o modelo do veículo (uma string).
#     ano: o ano de fabricação do veículo (um número inteiro). 
#     preco: o preço do veículo (um número decimal). 

class Veiculo:
    def __init__(self, modelo: str, ano: int, preco: float):
        self.modelo = modelo
        self.ano = ano
        self.preco = preco

# Na classe Veiculo, implemente um método chamado calcular_imposto() que retorna o imposto a ser pago pelo veículo. 
# O imposto é calculado como 10% do preço do veículo.

    def calcular_imposto(self):
        return (0.1 * self.preco)
    
    def info_modelo(self):
        return {self.modelo}
    
# Crie uma classe chamada Carro que herda da classe Veiculo. Adicione um atributo adicional:

#     marca: a marca do carro (uma string). 

class Carro(Veiculo):
    def __init__(self, modelo, ano, preco, marca):
        super().__init__(modelo, ano, preco)
        self.marca = marca

# Na classe Carro, implemente um método chamado desconto() que retorna um desconto de 5% no preço do carro.

    def desconto(self):
        novo_preco = (0.95 * self.preco)
        self.preco = novo_preco
        return self.preco

# Crie uma classe chamada Moto que também herda da classe Veiculo. Adicione um atributo adicional:

#     cilindrada: a cilindrada da moto (um número inteiro).

class Moto(Veiculo):
    def __init__(self, modelo, ano, preco, cilindrada):
        super().__init__(modelo, ano, preco)
        self.cilindrada = cilindrada

# Na classe Moto, implemente um método chamado calcular_imposto() que calcula o imposto a ser pago pela moto. 
# O imposto para motos é de 5% do preço do veículo.

    def calcular_imposto(self):
        return (0.05 * self.preco)
    
#  Crie instâncias de Carro e Moto, atribuindo valores adequados aos atributos de cada veículo.

veiculo1 = Carro('Uno', 2018, 40000, 'fiat')
veiculo2 = Carro('Brasilia', 1995, 55000, 'volkswagen')
veiculo3 = Moto('Yamaha', 2023, 22000, 300)
veiculo4 = Moto('Honda', 2015, 12000, 200) 

# Calcule e imprima o imposto a ser pago por cada veículo usando o método calcular_imposto().

veiculo1.desconto()
veiculo2.desconto()

print(f'Imposto para {veiculo1.info_modelo()} é igual a {veiculo1.calcular_imposto()}')
print(f'Imposto para {veiculo2.info_modelo()} é igual a {veiculo2.calcular_imposto()}')
print(f'Imposto para {veiculo3.info_modelo()} é igual a {veiculo3.calcular_imposto()}')
print(f'Imposto para {veiculo4.info_modelo()} é igual a {veiculo4.calcular_imposto()}')

## Alternativas:
# print('Imposto para', veiculo1.info_modelo(), 'é igual a: ', veiculo1.calcular_imposto())
# print('Imposto para', veiculo2.info_modelo(), 'é igual a: ', veiculo2.calcular_imposto())
# print('Imposto para', veiculo3.info_modelo(), 'é igual a: ', veiculo3.calcular_imposto())
# print('Imposto para', veiculo4.info_modelo(), 'é igual a: ', veiculo4.calcular_imposto())
