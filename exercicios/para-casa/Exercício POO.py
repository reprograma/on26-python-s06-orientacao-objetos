# Na classe Veiculo, implemente um método chamado calcular_imposto() que retorna o imposto a ser pago pelo veículo. 
# O imposto é calculado como 10% do preço do veículo.

#PASSO 1 - Criar a classe veículo que tem uma função de calcular o imposto
# CONSIDERAR
# modelo --> string
# preco --> float
# ano --> int

class Veiculo(): #calcular o imposto, preciso do preço do veículo, então vem antes o preço
    def __init__(self, modelo, preco, ano):
        self.modelo = modelo
        self.preco = preco
        self.ano = ano
    
    def calculo_de_imposto(imposto, self):
        imposto = 0.10*self.preco
        return imposto 

# PASSO 2 - Crie uma classe chamada Carro que herda da classe Veiculo. Adicione um atributo adicional:
# marca --> (uma string). 
# na classe Carro, além das três, ainda devo adiconar o atributo marca??

class Carro(Veiculo):
    def __init__(self, modelo, preco, ano, marca):
        self.modelo = modelo
        self.preco = preco
        self.ano = ano
        self.marca = marca
# Na classe Carro, implemente um método chamado desconto() que retorna um desconto de 5% no preço do carro. Criar função de desconto
    def descontar(desconto, self):
        desconto = 0.05*self.preco
        return desconto

#PASSO 3 - Crie uma classe chamada Moto que também herda da classe Veiculo. Adicione um atributo adicional:
# além de marca, adicionar o cilindrada ou adicionar no lugar da marca?? vou de 2°

#cilindrada --> int
# modelo --> string
# preco --> float
# ano --> int
#marca --> string
class Moto(Veiculo):
    def __init__(self, modelo, preco, ano, marca, cilindrada):
        self.modelo = modelo
        self.preco = preco
        self.ano = ano
        self.marca = marca
        self.cilindrada = cilindrada
# Na classe Moto, implemente um método chamado calcular_imposto(), o imposto para motos é de 5% do preço do veículo.
    def calculo_de_imposto(imposto, self):
        imposto_moto = 0.05*self.preco
        return imposto_moto

#Crie instâncias de Carro e Moto, atribuindo valores adequados aos atributos de cada veículo.
# Prof, se não tiver problema, quero dar uma decoradinha no meu código

escolha = input("Você quer obter informações sobre 'carro' ou 'moto'?")

if escolha == "carro":
    modelo_carro = input("Insira o modelo do carro: ")
    ano_carro = int(input("Insira o ano de fabricação do carro: "))
    preco_carro = float(input("Insira o preço do carro: "))
    marca_carro = input("Insira a marca do carro: ")    

elif escolha == "moto":
    modelo_moto = input("Digite o modelo da moto: ")
    ano_moto = int(input("Digite o ano de fabricação da moto: "))
    preco_moto = float(input("Digite o preço da moto: "))
    marca_moto= input("Insira a marca do moto: ")   
    cilindrada_moto = int(input("Digite a cilindrada da moto: "))   

else:
    print("Por favor, digite um nome válido")

# Crie instâncias de Carro e Moto, atribuindo valores adequados aos atributos de cada veículo
carros = Carro(modelo_carro, ano_carro, preco_carro, marca_carro)
motos = Moto(modelo_moto, ano_moto, preco_moto, marca_moto, cilindrada_moto)

# Calcule e imprima o imposto a ser pago por cada veículo usando o método:
print(f"Carro: {carros.modelo}, Marca: {carros.marca}, Preço: R${carros.preco}, Ano: {carros.ano} Desconto: R${carros.desconto()}, Imposto: R${carros.calcular_imposto()}")

print(f"Moto: {motos.modelo}, Marca: {motos.marca}, Cilindrada: {motos.cilindrada}, Ano: {motos.ano} Preço: R${motos.preco}, Imposto: R${motos.calcular_imposto()}")


