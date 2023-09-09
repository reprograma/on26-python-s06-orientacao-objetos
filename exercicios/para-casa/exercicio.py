class Veiculo:
    def __init__(self, modelo, ano, preco):
        self.modelo = modelo
        self.ano = ano
        self.preco = preco

    def calcular_imposto(self):
        return 0.10 * self.preco  

class Carro(Veiculo):
    def __init__(self, modelo, ano, preco, marca):
        super().__init__(modelo, ano, preco)
        self.marca = marca

    def calcular_desconto(self):
        return 0.05 * self.preco 

class Moto(Veiculo):
    def __init__(self, modelo, ano, preco, cilindrada):
        super().__init__(modelo, ano, preco)
        self.cilindrada = cilindrada

    def calcular_imposto(self):
        return 0.05 * self.preco 

carro1 = Carro("SUV", 2022, 250000.0, "Toyota")
moto1 = Moto("Esportiva", 2023, 15000.0, 600)

imposto_carro1 = carro1.calcular_imposto()
print(f"Imposto a ser pago pelo carro {carro1.marca} {carro1.modelo}: R$ {imposto_carro1:.2f}")


desconto_carro1 = carro1.calcular_desconto()
print(f"Desconto aplicado no carro {carro1.marca} {carro1.modelo}: R$ {desconto_carro1:.2f}")

# Calculando o imposto para a Moto
imposto_moto1 = moto1.calcular_imposto()
print(f"Imposto a ser pago pela moto (cilindrada {moto1.cilindrada}cc): R$ {imposto_moto1:.2f}")

