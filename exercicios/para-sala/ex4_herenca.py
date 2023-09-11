#Exercício 4 - Herança - Produto


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def descricao(self):
        return  f'Nome do produto: {self.nome}, Preço do produto: {self.preco}, '


class Produto_fisico(Produto):
    def __init__(self, nome, preco, peso, dimensao):
        super().__init__(nome, preco)
        self.peso = peso
        self.dimensao = dimensao

    def descricao(self):   
        return super().descricao()  + f'Peso do produto: {self.peso}, Dimensão do produto: {self.dimensao}'
    
class Produto_digital(Produto):
    def __init__(self, nome, preco, tamanho_arquivo):
        super().__init__(nome, preco)
        self.tamanho_arquivo = tamanho_arquivo

    def descricao(self):    
        return super().descricao() + f'Tamanho do arquivo: {self.tamanho_arquivo}.'    
    
  

produto_fisico_dani = Produto_fisico('Livro', 30.00, '1,2kg', '20 x 30')

print(produto_fisico_dani.descricao())

produto_digital_dani = Produto_digital('E-book', 25.99 , '10MB')

print(produto_digital_dani.descricao())
