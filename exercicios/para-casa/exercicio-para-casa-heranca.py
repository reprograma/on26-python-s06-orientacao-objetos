# ## 👩🏻‍💻 Crie uma classe base chamada Veiculo com os seguintes atributos:
# - modelo: o modelo do veículo (uma string).
# - ano: o ano de fabricação do veículo (um número inteiro).
# preco: o preço do veículo (um número decimal).
# Na classe Veiculo, implemente um método chamado `calcular_imposto()` que retorna o imposto a ser pago pelo veículo. 
#O imposto é calculado como 10% do preço do veículo.
# Crie uma classe chamada Carro que herda da classe Veiculo. Adicione um atributo adicional:
# - marca: a marca do carro (uma string).
# Na classe Carro, implemente um método chamado desconto() que retorna um desconto de 5% no preço do carro.
# Crie uma classe chamada Moto que também herda da classe Veiculo. Adicione um atributo adicional:
# - cilindrada: a cilindrada da moto (um número inteiro).
# Na classe Moto, implemente um método chamado `calcular_imposto()` que calcula o imposto a ser pago pela moto. 
#O imposto para motos é de 5% do preço do veículo.
# Crie instâncias de Carro e Moto, atribuindo valores adequados aos atributos de cada veículo.
# Calcule e imprima o imposto a ser pago por cada veículo usando o método `calcular_imposto()`.

class Veiculo:
    def __init__(self, modelo, ano, preco):
        self.modelo = modelo
        self.ano = ano
        self.preco = preco
    
    def descricao(self):
        return f"Modelo: {self.modelo}, ano: {self.ano}, preço: {self.preco}"
    
    def calcular_imposto(self):
        imposto = self.preco*0.1
        return imposto

class Carro(Veiculo):                                    #para calcular o imposto sobre o carro basta chamar o método criado na superclass, assim: print(nome_do_objeto.calcular_imposto())
    def __init__(self, modelo, ano, preco, marca):
        super().__init__(modelo, ano, preco)
        self.marca = marca                                  #super(): função usada pra chamar método incorporado na classe-mãe
        
     
    def descricao(self):
        return f"{super().descricao()}, marca: {self.marca}"
     
    def desconto(self):                                  #função que retorna o preço do carro depois de descontados o imposto e o desconto de 5%
        return f"O preço do veículo com o desconto é: {(super().calcular_imposto() + self.preco)*0.95}"                          # (preco + preco*0.1)*0.95
         

class Moto(Veiculo):
    def __init__(self, modelo, ano, preco, cilindrada):
        super().__init__(modelo, ano, preco)
        self.cilindrada = cilindrada
        
    
    def descricao(self):
        return f"{super().descricao()} e cilindrada: {self.cilindrada}."
    
    def calcular_imposto(self):
        imposto_moto = self.preco*0.05
        return f"Valor do imposto sobre a moto: {imposto_moto}."

#Exemplo
moto = Moto("ab", 2021, 10000.0, 20)

print(moto.calcular_imposto())
print(moto.descricao())