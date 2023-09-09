# Exercicio 2: Produtos

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def descricao(self):
        return f'Nome: {self.nome}, Preço R$ {self.preco}'
    
class ProdutoFisico(Produto):
    def __init__(self, nome, preco, peso, dimensoes):
        super().__init__(nome, preco)
        self.peso = peso
        self.dimensoes = dimensoes

    def descricao(self):
        return super().descricao() + f', Peso: {self.peso} kg, Dimensões: {self.dimensoes} cm'
    
produto_fisico_jessica = ProdutoFisico('Livro', 30.00, 0.5, '20x15x3')

print(produto_fisico_jessica.descricao())
