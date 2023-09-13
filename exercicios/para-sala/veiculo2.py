class Veiculo:
    def __init__(self, modelo, ano_veiculo, preco_veiculo):
        self.modelo = modelo
        self.ano_veiculo = ano_veiculo
        self.preco_veiculo = preco_veiculo

    def calcular_imposto(self):
        # 10% do preço do veículo.
        imposto = self.preco_veiculo * 0.10
        return imposto

    def __str__(self):
        return f"Modelo: {self.modelo}, Ano: {self.ano_veiculo}, Preço: R${self.preco_veiculo:.2f}"


class Carro(Veiculo):
    def __init__(self, modelo, ano_veiculo, preco_veiculo, marca):
        super().__init__(modelo, ano_veiculo, preco_veiculo)
        self.marca = marca

    def desconto(self):
        # 5% no preço do carro.
        desconto = self.preco_veiculo * 0.05
        return self.preco_veiculo - desconto

    def __str__(self):
        return f"Carro - Marca: {self.marca}, {super().__str__()}"


class Moto(Veiculo):
    def __init__(self, modelo, ano_veiculo, preco_veiculo, cilindrada):
        super().__init__(modelo, ano_veiculo, preco_veiculo)
        self.cilindrada = cilindrada

    def calcular_imposto(self):
        # 5% do preço do veículo para motos.
        imposto = self.preco_veiculo * 0.05
        return imposto

    def __str__(self):
        return f"Moto - Cilindrada: {self.cilindrada} cc, {super().__str__()}"


# Criando instâncias de Carro e Moto
carro_carol = Carro('HB20', 2023, 140000.00, 'Hyundai')
moto_carol = Moto('PCX', 2023, 26000.00, 150)

# Imprimindo as informações dos veículos
print("Descrição do Carro:")
print(carro_carol)
print(f"Imposto do Carro: R${carro_carol.calcular_imposto():.2f}")
print(f"Preço com Desconto do Carro: R${carro_carol.desconto():.2f}")
print("**************************")
print("Descrição da Moto")
print(moto_carol)
print(f"Imposto da Moto: R${moto_carol.calcular_imposto():.2f}")
