# EXERCÍCIOS ENCAPSULAMENTO

#     Exercício 1: Catálogo de Produtos

# Crie uma classe chamada Produto que represente um produto em um catálogo. 
# A classe deve ter os seguintes atributos privados:

# nome: o nome do produto. 
# preco: o preço do produto. 

class Produto:
    def __init__(self, nome: str, preco: float):
        self.__nome = nome
        self.__preco = preco

# A classe deve incluir métodos públicos para definir e obter o nome e o preço do produto. 

    def get_nome(self):
        return f'O nome do produto é: {self.__nome}'
    
    def set_nome(self, novo_nome):
        if len(novo_nome) > 0:
            self.__nome = novo_nome
            print(f'Nome atualizado com sucesso. Novo nome: {self.__nome}')
        
    def get_preco(self):
        return f'O preço do produto é: {self.__preco}'
    
    def set_preco(self, novo_preco):
        if novo_preco >= 0:
            self.__preco = novo_preco
            print(f'Preço atualizado com sucesso. Novo preço: {self.__preco}')

# Além disso, crie um método __str para exibir o produto de forma amigável.

    def __str__(self):
        return f'Produto: {self.__nome} Preço: {self.__preco}'
    
 #Criando instâncias de produto
produto1 = Produto('Perfume', 40)
produto2 = Produto('Hidratante', 10)

#Usando método __str__() para exibir todos atributos dos objetos
print(produto1.__str__())
print(produto2.__str__())

#Usando métodos get para exibir atributos específicos
print(produto1.get_nome())
print(produto2.get_preco())

# Atribuindo novos valores (a função já espera parâmetros específicos) 

produto1.set_nome('Perfume chique')
produto2.set_preco(15)

#Usando o método get_nome() para exibir atributo sobrescrito
print(produto1.get_nome())
print(produto2.get_preco())

#     Exercício 2: Biblioteca

# Crie uma classe chamada Livro que represente um livro em uma biblioteca. 
# A classe deve ter os seguintes atributos privados:

# titulo: o título do livro. 
# autor: o autor do livro. 
# _disponivel: um indicador de disponibilidade do livro 
# (inicialmente definido como True se o livro estiver disponível para empréstimo). 

class Livro:
    def __init__(self, titulo, autor, _disponivel):
        self.__titulo = titulo
        self.__autor = autor
        self._disponivel = _disponivel

# A classe deve incluir métodos públicos para emprestar o livro (definindo _disponivel como False) 
# e devolvê-lo (definindo _disponivel como True). 

    def emprestar_livro(self):
        self._disponivel = False

    def devolver_livro(self):
        self._disponivel = True

# Além disso, crie um método __str para exibir informações sobre o livro.

    def __str__(self):      
        if self._disponivel:
            return f'O livro {self.__titulo}, do(a) autor(a) {self.__autor} está disponível'
        else: 
            return f'O livro {self.__titulo}, do(a) autor(a) {self.__autor} não está disponível'
        
#Criando instâncias da classe Livro
livro1 = Livro('Memórias póstumas de Brás Cubas', 'Machado de Assis', True)
livro2 = Livro('A paixão segundo G.H.', 'Clarice Lispector', False)

#Imprimindo a função __str__ que exibe os atributos do objeto
print(livro1.__str__())
print(livro2.__str__())

#Emprestando um livro e logo em seguida exibindo seus atributos
livro1.emprestar_livro()
print(livro1)

#Devolvendo um livro e logo em seguida exibindo seus atributos
livro2.devolver_livro()
print(livro2)

#     Exercício 3: Banco de Dados de Funcionários

# Crie uma classe chamada Funcionario que represente um funcionário em um banco de dados de funcionários. 
# A classe deve ter os seguintes atributos privados:

# nome: o nome do funcionário. 
# cargo: o cargo do funcionário.

# A classe deve incluir métodos públicos para definir e obter o nome e o cargo do funcionário. 
# Além disso, crie um método __str para exibir informações sobre o funcionário.

class Funcionario:
    def __init__(self, nome: str, cargo: str):
        self.__nome = nome
        self.__cargo = cargo

    def set_nome(self, novo_nome):
        if len(novo_nome) > 0:
            self.__nome = novo_nome
            print(f'Nome atualizado no sistema com sucesso. Novo nome: {self.__nome}')

    def set_cargo(self, novo_cargo):
        if len(novo_cargo) > 0:
            self.__cargo = novo_cargo
            print(f'Cargo atualizado no sistema com sucesso. Novo cargo: {self.__cargo}')

    def get_nome(self):
        return f'O nome do funcionário é: {self.__nome}'

    def get_cargo(self):
        return f'O cargo do funcionário é: {self.__cargo}'
    
    def __str__(self):
        return f'Funcionário: {self.__nome} Cargo: {self.__cargo}'

funcionario1 = Funcionario('Andrea', 'Presidente')
funcionario2 = Funcionario('Bianca', 'CEO')
funcionario3 = Funcionario('Carlinhos', 'Líder de projeto')

print(funcionario1.__str__())
print(funcionario2.__str__())
print(funcionario3.__str__())

# Usando a função get para localizar um atributo específico:

print(funcionario2.get_nome())

# Usando a função set para atualizar o valor de um dos atributos:

funcionario3.set_cargo('Líder sênior de projeto')

print(funcionario3.__str__())

# EXERCÍCIOS ABSTRAÇÃO

#     Exercício 1: Figuras Geométricas

# Crie uma classe abstrata chamada FiguraGeometrica com um método abstrato calcular_area(). 
# Em seguida, crie subclasses concretas como Retangulo, Circulo e Triangulo que herdam da classe FiguraGeometrica. 
# Cada uma das subclasses deve implementar o método calcular_area() de acordo com a fórmula apropriada para cada figura geométrica.

import math

valor_pi = math.pi

class FiguraGeometrica:
    def __init__(self):
        pass

    def calcular_area(self):
        pass

class Retangulo(FiguraGeometrica):
    def __init__(self, largura, comprimento):
        super().__init__()
        self.largura = largura
        self.comprimento = comprimento

    def calcular_area(self):
        return self.largura * self.comprimento

class Circulo(FiguraGeometrica):
    def __init__(self, raio):
        super().__init__()
        self.raio = raio

    def calcular_area(self):
        return (valor_pi * self.raio ** 2)

class Triangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        super().__init__()
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura / 2)

figura1 = Retangulo(2, 30)
figura2 = Circulo(5)
figura3 = Triangulo(5, 3)

print(f'A área da figura {figura1.__class__.__name__} é igual a {figura1.calcular_area()}')
print(f'A área da figura {figura2.__class__.__name__} é igual a {figura2.calcular_area()}')
print(f'A área da figura {figura3.__class__.__name__} é igual a {figura3.calcular_area()}')

#     Exercício 2: Animais

# Crie uma classe abstrata chamada Animal com métodos abstratos emitir_som() e mover(). 
#Em seguida, crie subclasses concretas como Cachorro, Gato e Pato que herdam da classe Animal. 
#Cada uma das subclasses deve implementar os métodos emitir_som() e mover() 
#de acordo com o comportamento apropriado para cada animal.

class Animal:
    def __init__(self):
        pass

    def emitir_som(self):
        pass

    def mover(self):
        pass

class Cachorro(Animal):
    def __init__(self):
        super().__init__()

    def emitir_som(self):
        return print(f'O animal {__class__.__name__} emite um latido')
    
    def mover(self):
        return print(f'O animal {__class__.__name__} se move rapidamente')
    
class Pato(Animal):
    def __init__(self):
        super().__init__()

    def emitir_som(self):
        return print(f'O animal {__class__.__name__} emite um quáquá')
    
    def mover(self):
        return print(f'O animal {__class__.__name__} se move de forma desengonçada')
    
animal1 = Cachorro()
animal2 = Pato()

animal1.emitir_som()
animal1.mover()
animal2.emitir_som()
animal2.mover()