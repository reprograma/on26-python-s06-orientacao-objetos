"""Exercicio 1 - Herança"""

"""class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def descricao(self):
        return f"Marca: {self.marca}\nModelo: {self.modelo}\nAno: {self.ano}"


class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, numero_portas):
        super().__init__(marca, modelo, ano)
        self.numero_portas = numero_portas

    def descricao(self):
        return f"Tipo: Carro\n{super().descricao()}\nNúmero de Portas: {self.numero_portas}"


class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, tipo_motor):
        super().__init__(marca, modelo, ano)
        self.tipo_motor = tipo_motor

    def descricao(self):
        return f"Tipo: Moto\n{super().descricao()}\nTipo de Motor: {self.tipo_motor}"


# Exemplo de uso
carro = Carro("Toyota", "Corolla", 2022, 4)
moto = Moto("Honda", "CBR 600RR", 2021, "4 cilindros")

print(carro.descricao())

print(moto.descricao())"""

"""Exercicio 2"""

"""class Produto:
    def __init__(self,nome, preco):
        self.nome = nome
        self.preco = preco

    def descricao(self):
        return f"Nome: {self.nome}\nPreco: R${self.preco}"
    
class ProdutoFisico(Produto):
    def __init__(self,nome, preco, peso, dimensoes):
        super().__init__(nome, preco)
        self.peso = peso
        self.dimensoes = dimensoes

    def descricao(self):
        return f"Produto: ProdutoFisico\n{super().descricao()}\npeso: {self.peso}\ndimensoes: {self.dimensoes}"

class ProdutoDigital(Produto):
    def __init__(self,nome, preco, tamanho_arquivo):
        super().__init__(nome, preco)
        self.tamanho_arquivo = tamanho_arquivo
        
    def descricao(self):
        return f"Produto: ProdutoDigital\n{super().descricao()}\ntamanho_arquivo: {self.tamanho_arquivo}"

# Exemplo de uso
produto_fisico = ProdutoFisico("Quadro", 69.90, 1.5, "50x45x3")

print("Informações do Produto Físico:")
print(produto_fisico.descricao())

produto_digital = ProdutoDigital("Battlefield", 229.90, "1gb")

print("Informações do Produto Digital")
print(produto_digital.descricao())"""


"""Exercicio Extra  - Herança"""

class Imovel:
    def __init__(self, nome_do_proprietario, endereco, preco_base):
        self.nome_do_proprietario = nome_do_proprietario
        self.endereco = endereco
        self.preco_base = preco_base
    

    def calcular_aluguel(self):
        return self.preco_base
    
class Casa(Imovel):
    def __init__(self,nome_do_proprietario, endereco, preco_base, area_terreno):
        super().__init__(nome_do_proprietario, endereco, preco_base)
        self.area_terreno = area_terreno

    def calcular_aluguel(self):
        resp = self.preco_base + (self.area_terreno * 5)
        return resp
       
class Apartamento(Imovel):
    def __init__(self,nome_do_proprietario, endereco, preco_base, numero_quartos):
        super().__init__(nome_do_proprietario, endereco, preco_base)
        self.numero_quartos = numero_quartos
   
    def calcular_aluguel(self):
        resp = self.preco_base + (self.numero_quartos * 300)
        return resp
    

# Exemplo de Uso

casa_maria = Casa("Maria da Conceição", "Rua das Orquídeas, 32, Cidade Jardim", 1.000, 600)
apartamento_carlos = Apartamento("Carlos José", "Av. Oceânica, 288, Piatã", 1.300, 3)

print(casa_maria.calcular_aluguel())
print(apartamento_carlos.calcular_aluguel())