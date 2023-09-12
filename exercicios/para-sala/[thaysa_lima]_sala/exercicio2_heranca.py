# - Exercício 2: Produtos
# Crie um sistema de gerenciamento de produtos em uma loja. Crie uma classe base chamada Produto com os seguintes atributos:
# nome: o nome do produto.
# preco: o preço do produto.
# A classe Produto deve ter um método chamado `descricao()` que retorna uma descrição completa do produto.
# Crie duas subclasses concretas, ProdutoFisico e ProdutoDigital, que herdam da classe Produto. Adicione atributos específicos para cada tipo de produto, como peso e dimensões para produtos físicos e tamanho de arquivo para produtos digitais.
# Implemente o método `descricao()` em cada uma das subclasses para incluir informações específicas do tipo de produto.
# Crie instâncias de ProdutoFisico e ProdutoDigital, atribuindo valores adequados aos atributos de cada produto. Use o método `descricao()` para exibir informações detalhadas sobre cada produto.
# Esses exercícios ajudarão você a praticar a criação de hierarquias de classes com herança em Python e a entender como compartilhar funcionalidades comuns e adicionar comportamentos específicos em subclasses.

class Produtos:
    def __init__(self, nome_prod, preco_prod):
        self.nome = nome_prod
        self.preco = preco_prod

    def descricao(self):
        return (f"Nome Produto: {self.nome}, Preço Produto: R${self.preco:.2f}")
    
class ProdutoFisico(Produtos):
    def __init__(self, nome_prod, preco_prod, tamanho_prod, peso_prod):
        super().__init__(nome_prod, preco_prod)
        self.tamanho_prod = tamanho_prod
        self.peso_prod = peso_prod

    def descricao(self):
        return f"Produto Físico - {super().descricao()}, Tamanho do produto: {self.tamanho_prod}cm, Peso: {self.peso_prod}g"

class ProdutoDigital(Produtos):
    def __init__(self, nome_prod, preco_prod, tamanho_aquivo_prod):
        super().__init__(nome_prod, preco_prod)
        self.tamanho_arquivo_prod = tamanho_aquivo_prod

    def descricao(self):
        return f"Produto Digital - {super().descricao()}, Tamanho do Arquivo: {self.tamanho_arquivo_prod} MB"
    
#Exemplos de como chamar, criando instâncias
produto_fisico = ProdutoFisico("Pintura", 15.00, "15x20x2", 100)
produto_digital = ProdutoDigital("Pintura Digital", 9.99, 5.2)

print(produto_fisico.descricao())
print(produto_digital.descricao())
