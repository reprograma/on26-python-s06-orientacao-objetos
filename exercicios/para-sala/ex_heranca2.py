class Produtos:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def descricao(self):
        return f'Nome: {self.nome}, Preco: {self.preco}'
    
class ProdutoFisico(Produtos):
    def __init__(self, nome, preco, peso, dimensoes):
        super().__init__(nome, preco)
        self.peso = peso
        self.dimensoes = dimensoes

    def descricao(self):
        return super().descricao() + f', Peso: {self.peso}, Dimensões: {self.dimensoes}'
    
class ProdutoDigital(Produtos):
    def __init__(self, nome, preco, tamanho_arquivo):
        super().__init__(nome, preco)
        self.tamanho_arquivo = tamanho_arquivo

    def descricao(self):
        return super().descricao() + f', Tamanho do Arquivo: {self.tamanho_arquivo}'
    
fisico = ProdutoFisico('Livro', 19.0, 2, '3x2')

digital = ProdutoDigital('Ebook', 10.0, '2KB')

print(fisico.descricao())

print(digital.descricao())