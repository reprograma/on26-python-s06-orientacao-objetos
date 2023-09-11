#Exercício Herança

class Veiculo: 
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def descricao(self):
        return f'Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, '    

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, portas):
        super().__init__(marca, modelo, ano)
        self.portas = portas

    def descricao(self):
        return super().descricao() + f'Número de portas: {self.portas}'
    


class Moto(Veiculo):  
    def __init__(self, marca, modelo, ano, motor_cc):
        super().__init__(marca, modelo, ano)  
        self.motor_cc = motor_cc

    def descricao(self):
        return super().descricao() + f'Tipo de motor: {self.motor_cc} cilindradas'


carro_dani = Carro('Toyota', 'Corolaa', 2023, 4)

moto_dani = Moto('Honda', 'CBR500R', 2022, 500)

print(f'Segue as descrições do veículo: {carro_dani.descricao()}')
print(f'Segue as descrições do veículo: {moto_dani.descricao()}')

