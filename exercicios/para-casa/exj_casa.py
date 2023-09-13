## Exercício de Casa 🏠 
## 👩🏻‍💻 Crie uma classe base chamada Veiculo com os seguintes atributos:

# - modelo: o modelo do veículo (uma string).
# - ano: o ano de fabricação do veículo (um número inteiro).
# preco: o preço do veículo (um número decimal).
# Na classe Veiculo, implemente um método chamado `calcular_imposto()` que retorna o imposto a ser pago 
# pelo veículo. O imposto é calculado como 10% do preço do veículo.

# Crie uma classe chamada Carro que herda da classe Veiculo. Adicione um atributo adicional:
# - marca: a marca do carro (uma string).
# Na classe Carro, implemente um método chamado desconto() que retorna um desconto de 5% no preço do carro.

# Crie uma classe chamada Moto que também herda da classe Veiculo. Adicione um atributo adicional:
# - cilindrada: a cilindrada da moto (um número inteiro).

# Na classe Moto, implemente um método chamado `calcular_imposto()` que calcula o imposto a ser pago 
# pela moto. O imposto para motos é de 5% do preço do veículo.

# Crie instâncias de Carro e Moto, atribuindo valores adequados aos atributos de cada veículo.
# Calcule e imprima o imposto a ser pago por cada veículo usando o método `calcular_imposto()`.


class Veiculos:
    def __init__(self, modelo, ano, preco):
        self.modelo = modelo
        self.ano = ano
        self.preco = preco
        
    def calcular_imposto(self):
        return self.preco * 0.10
        
        
class Carro(Veiculos):
    def __init__(self, modelo, ano, preco, marca):
        super().__init__(modelo, ano, preco)
        self.marca = marca
                   
    def desconto(self):
        return self.preco - (self.preco * 0.05)


class Moto(Veiculos):
    def __init__(self, modelo, ano, preco, cilindrada):
        super().__init__(modelo, ano, preco)
        self.cilindrada = cilindrada
        
    def calcular_imposto(self):
        return self.preco * 0.05
    
    
carro_julia = Carro("C3", 2018, 20000, "Citroen")
moto_pablo = Moto("Lander", 2020, 15000, "Yamaha")

print(carro_julia.calcular_imposto())
print(moto_pablo.calcular_imposto())