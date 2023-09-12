class Veiculo:
    def __init__(self,modelo, ano, preco_base):
        self.modelo = modelo
        self.ano = ano
        self.preco_base = preco_base
        
    def calcular_imposto(self):
            return self.preco_base * 0.10
        
class Carro(Veiculo):
    def __init__(self,modelo, ano, preco_base, marca):
        super().__init__(modelo, ano, preco_base)
        self.marca = marca
        
    def desconto(self):
        return self.preco_base * 0.05
    
class Moto(Veiculo):
    def __init__(self,modelo, ano, preco_base, cilindrada):
        super().__init__(modelo, ano, preco_base)
        self.cilindrada = cilindrada
        
    def calcular_imposto(self):
        return self.preco_base * 0.05
    
carro_1 = Carro("Corolla", 2023, 125.000, "Toyota")
moto_1 = Moto("XT", 2023, 15.000, 660)

print(f"Carro - Modelo: {carro_1.modelo}, Ano: {carro_1.ano}, Marca: {carro_1.marca}, Imposto a ser pago: R${carro_1.calcular_imposto()}")
print(f"Moto - Modelo: {moto_1.modelo}, Ano: {moto_1.ano}, Cilindrada: {moto_1.cilindrada}cc, Imposto a ser pago: R${moto_1.calcular_imposto()}")