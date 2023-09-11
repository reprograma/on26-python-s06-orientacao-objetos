# 👩🏻‍💻 Crie uma classe base chamada Veiculo com os seguintes atributos:
# 1-Modelo: o modelo do veículo (uma string).
# 2-Ano: o ano de fabricação do veículo (um número inteiro). 
# 3-Preço: o preço do veículo (um número decimal). 
# 4-Na classe Veiculo, implemente um método chamado calcular_imposto() que retorna o imposto a ser pago pelo veículo. O imposto é calculado como 10% do preço do veículo.
# 5-Crie uma classe chamada Carro que herda da classe Veiculo. Adicione um atributo adicional:
# 5.1-Marca: a marca do carro (uma string). 
# 5.2 Na classe Carro, implemente um método chamado desconto() que retorna um desconto de 5% no preço do carro.
# 6-Crie uma classe chamada Moto que também herda da classe Veiculo. 
# 6.1-Adicione um atributo adicional:
# 6.2-Cilindrada: a cilindrada da moto (um número inteiro). Na classe Moto, implemente um método chamado calcular_imposto() que calcula o imposto a ser pago pela moto. O imposto para motos é de 5% do preço do veículo.
# 7-Crie instâncias de Carro e Moto, atribuindo valores adequados aos atributos de cada veículo.
# 8-Calcule e imprima o imposto a ser pago por cada veículo usando o método calcular_imposto().


class Veiculo:
  def __init__(self, modelo, ano, preco):
    self.modelo = modelo 
    self.ano = ano 
    self.preco = preco
    
  def calcular_imposto(self):
    imposto_a_ser_pago = self.preco * 0.1
    return imposto_a_ser_pago

class Carro(Veiculo):
  def __init__(self, modelo,ano,preco,marca):
      super().__init__(modelo,ano,preco)
      self.marca = marca

  def desconto(self):
    desconto_carro = self.preco * 0.05
    return desconto_carro


class Moto(Veiculo):
  def __init__(self, modelo,ano,preco,cilindrada):
    super().__init__(modelo,ano,preco)
    self.cilindrada = cilindrada
  def calcular_imposto(self):
    imposto_moto = self.preco * 0.05
    return imposto_moto

carro=Carro("Ford Ka", 2015, 120.000, "Ford")
moto=Moto("Honda Bis", 2015, 45.000, "Honda")

imposto_carro = carro.calcular_imposto()
imposto_moto = moto.calcular_imposto()
desconto_carro = carro.desconto()

print(f"Imposto do carro: R${imposto_carro:.4f}")
print(f"Imposto da moto: R${imposto_moto:.3f}")
print(f"Desconto do carro: R${desconto_carro:.4f}") 
