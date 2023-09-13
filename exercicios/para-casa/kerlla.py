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

    def desconto(self):
        return 0.05 * self.preco

class Moto(Veiculo):
    def __init__(self, modelo, ano, preco, cilindrada):
        super().__init__(modelo, ano, preco)
        self.cilindrada = cilindrada

    def calcular_imposto(self):
        return 0.05 * self.preco

carro1 = Carro("BMW iX3", 2022, 130000.00, "BMW")
moto1 = Moto("Scooter", 2023, 6000.00, 600)

imposto_carro = carro1.calcular_imposto()
imposto_moto = moto1.calcular_imposto()

print(f"Imposto a ser pago pelo carro: R${imposto_carro:.2f}")
print(f"Imposto a ser pago pela moto: R${imposto_moto:.2f}")



