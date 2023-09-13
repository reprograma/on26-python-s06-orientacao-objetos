'''
Classe veículo com os seguintes atributos: modelo (str), ano(int) preço(float)
Na classe Veiculo, implemente um método chamado `calcular_imposto()` que retorna o imposto a ser pago pelo veículo. 
O imposto é calculado como 10% do preço do veículo. 
Crie uma classe chamada Carro que herda da classe Veiculo. Adicione um atributo adicional:
marca: a marca do carro
Na classe Carro, implemente um método chamado desconto() que retorna um desconto de 5% no preço do carro.
Crie uma classe chamada Moto que também herda da classe Veiculo. Adicione um atributo adicional:
cilindrada: a cilindrada da moto. 
Na classe Moto, implemente um método chamado `calcular_imposto()` que calcula o imposto a ser pago pela moto. O imposto para motos é de 5% do preço do veículo.
Crie instâncias de Carro e Moto, atribuindo valores adequados aos atributos de cada veículo.
Calcule e imprima o imposto a ser pago por cada veículo usando o método `calcular_imposto()`.
'''
class veiculo:
    def __init__(self, modelo, ano, preco):
        self.modelo = modelo
        self.ano = ano
        self.preco = preco
        
    def calcular_imposto(self):
        return 0.1 * self.preco

class carro(veiculo):
    def __init__(self, modelo, ano, preco, marca):
        super().__init__(modelo, ano, preco)
        self.marca = marca

    def desconto(self):
        return 0.05 * self.preco

class moto(veiculo):
    def __init__(self, modelo, ano, preco, cilindrada):
        super().__init__(modelo, ano, preco)
        self.cilindrada = cilindrada

    def calcular_imposto(self):
        return 0.05 * self.preco

carro1 = carro("Sedan", 2022, 30000, "Toyota")
moto1 = moto("XRE", 2022, 20000, "Honda")

imposto_carro1 = carro1.calcular_imposto()
desconto_carro1 = carro1.desconto()
imposto_moto1 = moto1.calcular_imposto()

print(f"Carro - Marca: {carro1.marca}, Imposto a ser pago: R${imposto_carro1}, Desconto: R${desconto_carro1}")
print(f"Moto - Cilindrada: {moto1.cilindrada}, Imposto a ser pago: R${imposto_moto1}")
