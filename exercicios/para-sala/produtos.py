#Crie um sistema de gerenciamento de produtos em uma loja.
#Crie uma classe base chamada Produto com os seguintes atributos:

#nome: o nome do produto
#preco: o preço do produto.
#A classe Produto deve ter um método chamado descricao() que retorna uma descrição completa do produto.

#Crie duas subclasses concretas, ProdutoFisico e ProdutoDigital, que herdam da classe Produto.
#Adicione atributos específicos para cada tipo de produto, como peso e dimensões para produtos físicos e
#tamanho de arquivo para produtos digitais.

#Implemente o método descricao() em cada uma das subclasses para incluir informações específicas do tipo de produto.

#Crie instâncias de ProdutoFisico e ProdutoDigital, atribuindo valores adequados aos atributos de cada produto.
#Use o método descricao() para exibir informações detalhadas sobre cada produto.

#Esses exercícios ajudarão você a praticar a criação de hierarquias de classes com herança em Python
#e a entender como compartilhar funcionalidades comuns e adicionar comportamentos específicos em subclasses.

class produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class prodFis(produto):
    def __init__(self, nome, preco, volume):
        super().__init__(self, nome, preco)
        self.volume = volume

    def descricao(self):
        return f'{super().descricao()}'

class prodDig(produto):
    def __init__(self, nome, preco, tamanho):
        super().__init__(self, nome, preco)
        self.volume = volume

    def descricao(self):
        return f'{super().descricao()}'