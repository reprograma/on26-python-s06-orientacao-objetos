# Exercício 1

class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def info(self):
        print(f'Marca do veículo:', self.marca,),
        print(f'Modelo do veículo:', self.modelo),
        print(f'Ano de Fabricação:', self.ano)

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, numero_de_portas):
        super().__init__(marca, modelo, ano)
        self.numero_de_portas = numero_de_portas
    
    def info(self):
        super().info()
        print("Número de portas:", self.numero_de_portas)

carro_1 = Carro ('Audi', 'RSQ8', '2022', '4')

carro_1.info()

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, motor):
        super().__init__(marca, modelo, ano)
        self.motor = motor
    
    def info(self):
        super().info()
        print("Tipo de Motor:", self.motor)

moto_1 = Moto ('Honda', 'CB500', '2023', 'Bicilíndrico')

moto_1.info()


# Exercício 2

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        
    def info(self):
        print(f'Nome do Produto:', self.nome),
        print(f'Preço R$:', self.preco)

class ProdutoFisico(Produto):
    def __init__(self, nome, preco, peso, dimensao):
        super().__init__(nome, preco)
        self.peso = peso
        self.dimensao = dimensao
    
    def info(self):
        super().info()
        print("Peso:", self.peso)
        print("Dimensões:", self.dimensao)

produto_fisico_darla = ProdutoFisico ('Livro', 30.00, 0.5, '20X15X3')

produto_fisico_darla.info()


# Exercicio Extra

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
        resp =  self.preco_base + (self.area_terreno * 5)
        return resp
    
class Apartamento(Imovel):
    def __init__(self, endereco, nome_do_proprietario, preco_base, numero_quartos):
        super().__init__(endereco,nome_do_proprietario, preco_base)
        self.numero_quartos = numero_quartos
        
    def calcular_aluguel(self):
        resp =  self.preco_base + (self.numero_quartos * 300)
        return resp
    
    
casa_maria = Casa("122 Rua das Flores", "Maria", 1500, 300)
apartamento_carlos = Apartamento("333, Av. João Mendes", 'Carlos Jose', 1200, 2)


print(casa_maria.calcular_aluguel())