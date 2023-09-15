class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def descricao(self):
        return f'Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}'

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, num_portas):
        super().__init__(marca, modelo, ano)
        self.num_portas = num_portas

    def descricao(self):
        return super().descricao() + f', Números de portas: {self.num_portas}'
  
class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, tipo_motor):
        super().__init__(marca, modelo, ano)
        self.tipo_motor = tipo_motor

    def descricao(self):
        return super().descricao() + f', tipo de motor: {self.tipo_motor}'

carro = Carro('Toyota', 'Corolla', 2021, 4)

moto = Moto('honda', 'CBR500R', 2022, '4 tempos')

print(carro.descricao())

print(moto.descricao())