py#exercicio casa - Semana 6 -
class Veiculo:
 def __int__(self,modelo, ano, preço):
      self.modelo = modelo
      self.preço = preço
      self.ano = ano

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

carro = Carro("Clio", 2022, 30000.0,)
moto = Moto("Bis", 2021, 35000.0, 250)

imposto_carro = carro.calcular_imposto()
imposto_moto = moto.calcular_imposto()
#adicionei os modelos

print(f"Imposto do Carro: R$ {imposto_carro:.2f}")
print(f"Imposto da Moto: R$ {imposto_moto:.2f}")


