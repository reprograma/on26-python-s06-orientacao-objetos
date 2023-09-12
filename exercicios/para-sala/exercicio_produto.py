'''
Crie um sistema de gerenciamento de produtos em uma loja. Crie uma classe base chamada Produto com os seguintes atributos:

nome: o nome do produto.
preco: o preço do produto.

A classe Produto deve ter um método chamado `descricao()` que retorna uma descrição completa do produto.
Crie duas subclasses concretas, ProdutoFisico e ProdutoDigital, que herdam da classe Produto. 
Adicione atributos específicos para cada tipo de produto, como peso e dimensões para produtos físicos e tamanho de arquivo para produtos digitais.

Implemente o método `descricao()` em cada uma das subclasses para incluir informações específicas do tipo de produto.
Crie instâncias de ProdutoFisico e ProdutoDigital, atribuindo valores adequados aos atributos de cada produto. 
Use o método `descricao()` para exibir informações detalhadas sobre cada produto.
'''
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def descricao(self):
        return f"Nome do produto: {self.nome}.\nPreço do produto: R${self.preco}"
    
class ProdutoFisico(Produto):
    def __init__(self, nome, preco, peso, dimensoes):
        super().__init__(nome, preco)
        self.peso = peso
        self.dimensoes = dimensoes

    def descricao(self):
        return super().descricao()
    
class ProdutoDigital(Produto):
    def __init__(self, nome, preco, tamanho_arquivo):
        super().__init__(nome, preco)
        self.tamanho_arquivo = tamanho_arquivo

    def descricao(self):
        return super().descricao() + f", Tamanho do Arquivo: {self.tamanho_arquivo} MB"
    
produto_fisico_darla = ProdutoFisico("livro", 50, 0.5, "10x15x3")

print(produto_fisico_darla.descricao())

produto_digital_darla = ProdutoDigital("E-book", 50, 10)

print(produto_digital_darla.descricao())
