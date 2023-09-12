class Veiculos:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def descricao(self):
        text = f'Marca: {self.marca}, modelo: {self.modelo}, Ano: {self.ano}'
        print(text)

class Carro(Veiculos):
    def __init__(self, marca, modelo, ano, qtd_portas):
        super().__init__(marca, modelo, ano)
        self.qtd_portas = qtd_portas

    def descricao(self):
        text = f'{super().descricao()} Quantidade de portas: {self.qtd_portas}'
        print(text)

class Moto(Veiculos):
    def __init__(self, marca, modelo, ano, motor):
        super().__init__(marca, modelo, ano)
        self.motor = motor

    def descricao(self):
        text = f'Marca: {self.marca}, modelo: {self.modelo}, Ano: {self.ano}, O Motor: {self.motor}'
        print(text)

carro = Carro('fiat', 'uno', 1994, 2)
moto = Moto('honda', 'CBR50R', 2022, '4 tempos')

carro.descricao()
moto.descricao()

#exercico 2 produtos

class Produtos:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        
    def descricao(self):
        return f' nome: {self.nome}, Preço: {self.preco}'
    
class ProdutoFisico(Produtos):
    def __init__(self, nome, preco, peso, dimensoes):
        super().__init__(nome, preco)
        self.peso = peso
        self.dimensoes = dimensoes
    
    def descricao(self):
        return super().descricao() + f', Peso: [self.pes] kg, Dimensões: {self.dimensoes} cm'
    
class ProdutoDigital(Produtos):
    def __init__(self, nome, preco, tamanho_arquivo):
        super().__init__(nome, preco)
        self.tamanho_arquivo = tamanho_arquivo
    
    def descricao(self):
        return super.descricao() + f', Tamanho do arquivo {self.tamanho_arquivo}'

produto_fisico_darla = ProdutoFisico('livro', 30.00, 0.5, '20x15x3')

print(produto_fisico_darla.descricao())    

""" Implemente o método calcular_aluguel() em cada uma das subclasses para calcular o valor do aluguel com base em regras específicas:
Para Casa, o aluguel deve ser calculado como preco_base + (area_terreno * 5).
Para Apartamento, o aluguel deve ser calculado como preco_base + (numero_quartos * 300).
e superclass tem o atributo endereco e nome_do_proprietario"""

class Imovel:
    def __init__(self, endereco, nome_do_proprietario, preco_base):
        self.endereco = endereco
        self.nome_do_proprietario = nome_do_proprietario
        self.preco_base = preco_base
        
        def calcular_aluguel(self):
            return self.preco_base
        
class Casa(Imovel):
    def __init__(self, endereco, nome_do_proprietario, preco_base, area_terreno):
        super().__init__(endereco, nome_do_proprietario, preco_base)
        self.area_terreno = area_terreno
        
    def calcular_aluguel(self):
        return self.preco_base + (self.area_terreno * 5)

class Apartamento(Imovel):
    def __init__(self, endereco, nome_do_proprietario, preco_base, numero_quartos):
        super().__init__(endereco, nome_do_proprietario, preco_base)
        self.numero_quartos = numero_quartos
        
    def calcular_aluguel(self):
        return super().preco_base + (self.numero_quartos * 300)
    
casa_maria = Casa('122 Rua das flores', 'Maria', 1500, 300)
ape_carla = Apartamento('333 Rua bem te vi', 'Ana Carla', 1200, 2)

print(casa_maria.calcular_aluguel())