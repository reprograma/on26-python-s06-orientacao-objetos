

"""- modelo: o modelo do veículo (uma string).
- ano: o ano de fabricação do veículo (um número inteiro).
preco: o preço do veículo (um número decimal).
Na classe Veiculo, implemente um método chamado `calcular_imposto()` que retorna o imposto a ser pago pelo veículo. O imposto é calculado como 10% do preço do veículo.


Crie uma classe chamada Carro que herda da classe Veiculo. Adicione um atributo adicional:

- marca: a marca do carro (uma string).
Na classe Carro, implemente um método chamado desconto() que retorna um desconto de 5% no preço do carro.

Crie uma classe chamada Moto que também herda da classe Veiculo. Adicione um atributo adicional:

- cilindrada: a cilindrada da moto (um número inteiro).
Na classe Moto, implemente um método chamado `calcular_imposto()` que calcula o imposto a ser pago pela moto. O imposto para motos é de 5% do preço do veículo.

Crie instâncias de Carro e Moto, atribuindo valores adequados aos atributos de cada veículo.

Calcule e imprima o imposto a ser pago por cada veículo usando o método `calcular_imposto()`."""

class Veiculo:
    def __init__(self,modelo, ano, preco):
        self.modelo = modelo
        self.ano = ano 
        self.preco = preco


    def calcular_imposto(self):
        
        return f'Modelo do veículo: {self.modelo}, Ano do Veículo: {self.ano}, Preço do Veículo: R${self.preco}, Imposto do Veículo: R${self.preco * 0.1} '  
    
class Carro(Veiculo):
    def __init__(self, modelo, ano, preco, marca):
        super().__init__(modelo, ano, preco)
        self.marca = marca
    
    def desconto(self):
    
      return  f'Marca do Veículo: {self.marca}, Desconto do Veículo: R${self.preco * 0.05}'
    
class Moto(Veiculo):
    def __init__(self, modelo, ano, preco, marca, motor_cc):
        super().__init__(modelo, ano, preco)
        self.marca = marca
        self.motor_cc = motor_cc

    def calcular_imposto(self):

       return f'Modelo da Motocicleta: {self.modelo}, Ano da Motocicleta: {self.ano}, Preço da Motocicleta: R${self.preco}, Imposto da Motocicleta: R${self.preco * 0.05}'





carro_dani = Carro('Monza', 2006, 50000, 'Chevrolet')
print(carro_dani.calcular_imposto())  # Chame o método calcular_imposto() da classe Veiculo
print(carro_dani.desconto())  # Chame o método desconto() da classe Carro

moto_dani = Moto('XTZ', 2008, 15000, 'YAMAHA', '150cc')

print(moto_dani.calcular_imposto())



