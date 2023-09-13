#  Exercício 2: Produtos

# Crie um sistema de gerenciamento de produtos em uma loja. Crie uma classe base chamada Produto com os seguintes atributos:

# nome: o nome do produto.
# preco: o preço do produto.
# A classe Produto deve ter um método chamado `descricao()` que retorna uma descrição completa do produto.

# Crie duas subclasses concretas, ProdutoFisico e ProdutoDigital, que herdam da classe Produto. Adicione atributos 
# específicos para cada tipo de produto, como peso e dimensões para produtos físicos e tamanho de arquivo para produtos digitais.

# Implemente o método `descricao()` em cada uma das subclasses para incluir informações específicas do tipo de produto.

# Crie instâncias de ProdutoFisico e ProdutoDigital, atribuindo valores adequados aos atributos de cada produto. 
# Use o método `descricao()` para exibir informações detalhadas sobre cada produto.

# Esses exercícios ajudarão você a praticar a criação de hierarquias de classes com herança em Python 
# e a entender como compartilhar funcionalidades comuns e adicionar comportamentos específicos em subclasses.

# c
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        
    def descricao(self):
        return f'nome: {self.nome}, Preço R$ {self.preco}'
    
class ProdutoFisico(Produto):
    def __init__(self, nome, preco, peso, dimensoes):
        super().__init__(nome, preco)
        self.peso = peso
        self.dimensoes = dimensoes
        
        
    def descricao(self):
        return super().descricao() + f", Peso: {self.peso} kg, Dimensões: {self.dimensoes} cm"
    
class ProdutoDigital(Produto):
    def __init__(self, nome, preco, tamanho_arquivo):
        super().__init__(nome,preco)
        self.tamanho_arquivo = tamanho_arquivo
        
    def descricao(self):
        return super().descricao() + f", Tamanho do Arquivo: {self.tamanho_arquivo} MB"
    
    
produto_fisico_darla = ProdutoFisico('livro', 30.00, 0.5, '20x15x3')

print(produto_fisico_darla.descricao()) 

produto_digital_darla = ProdutoDigital('E-book', 50.00, 10)

print(produto_digital_darla.descricao())


