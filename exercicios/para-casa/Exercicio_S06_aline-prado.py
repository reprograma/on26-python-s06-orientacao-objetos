"""Resolução - Exercício de Casa"""

class Veiculo:
    def __init__(self, modelo, ano, preco):
        self.modelo = modelo
        self.ano = ano
        self.preco = preco

    def calcular_imposto(self):
        return self.preco * 0.10  # Imposto de 10% (Veiculo)


class Carro(Veiculo):
    def __init__(self, modelo, ano, preco, marca):
        super().__init__(modelo, ano, preco)
        self.marca = marca

    def desconto(self):
        return self.preco * 0.05  # Desconto de 5% (carro)

class Moto(Veiculo):
    def __init__(self, modelo, ano, preco, cilindrada):
        super().__init__(modelo, ano, preco)
        self.cilindrada = cilindrada

    def calcular_imposto(self):
        return self.preco * 0.05  # Imposto de 5% (moto)

# Instância de Carro  
carro1 = Carro("Corolla", 2023, 148900.0, "Toyota")

#Instância de moto 
moto1 = Moto("CG Titan", 2022, 30000.0, 167)

# Cãlculo dos Impostos
imposto_carro = carro1.calcular_imposto()
imposto_moto = moto1.calcular_imposto()

print(f"O imposto a ser pago para o carro ({carro1.modelo}), é de: R${imposto_carro:.2f}")
print(f"O imposto a ser pago para a moto ({moto1.modelo}),  é de: R${imposto_moto:.2f}")
