# Exercício de Herança em Python: Sistema de Gerenciamento de Funcionários (Exercicío Avançado Extra)

# Você está encarregado de criar um sistema de gerenciamento de funcionários para uma empresa. 
# O sistema deve ser capaz de lidar com diferentes tipos de funcionários 
# e calcular seus salários com base em suas características específicas. 
# Para isso, você precisa implementar a hierarquia de classes apropriada usando herança em Python.

# Instruções:

# Crie uma classe base chamada Funcionario com os seguintes atributos:
#     nome: o nome do funcionário.
#     salario: o salário base do funcionário (inicialmente definido como 0).

class Funcionario:
    def __init__(self, nome: str, salario: float):
        self.nome = nome
        self.salario = salario

# A classe Funcionario deve ter um método chamado calcular_pagamento() que retorna o pagamento do funcionário. 
# No entanto, este método deve ser definido como um método abstrato (utilizando pass) 
# uma vez que cada tipo de funcionário (temporário e integral) calculará o pagamento de maneira diferente.

    def calcular_pagamento(self):
        pass

    def get_nome(self):
        return self.nome

# Crie uma classe chamada FuncionarioTemporario, que herda da classe Funcionario. 
# Esta classe deve ter os seguintes atributos adicionais:
#     salario_por_hora: o salário por hora do funcionário temporário.
#     horas_trabalhadas: o número de horas trabalhadas pelo funcionário temporário. 

class FuncionarioTemporario(Funcionario):
    def __init__(self, nome, salario, salario_por_hora, horas_trabalhadas):
        super().__init__(nome, salario)
        self.salario_por_hora = salario_por_hora
        self.horas_trabalhadas = horas_trabalhadas

# Na classe FuncionarioTemporario, implemente o método calcular_pagamento() 
# para calcular o pagamento do funcionário temporário com base no salário por hora e nas horas trabalhadas.

    def calcular_pagamento(self):
        return (self.salario_por_hora * self.horas_trabalhadas)

# Crie uma classe chamada FuncionarioIntegral, que também herda da classe Funcionario. 
# Esta classe deve ter um atributo adicional:
#     salario_mensal: o salário mensal do funcionário integral. 

class FuncionarioIntegral(Funcionario):
    def __init__(self, nome, salario, salario_mensal):
        super().__init__(nome, salario)
        self.salario_mensal = salario_mensal

# Na classe FuncionarioIntegral, implemente o método calcular_pagamento() 
# para calcular o pagamento do funcionário integral, que é igual ao seu salário mensal.

    def calcular_pagamento(self):
        return self.salario_mensal
    
# Crie instâncias de FuncionarioTemporario e FuncionarioIntegral, 
# atribuindo valores adequados aos atributos de cada funcionário.

funcionario1 = FuncionarioIntegral('Armando', 0, 3000)
funcionario2 = FuncionarioIntegral('Bento', 0, 3500)
funcionario3 = FuncionarioTemporario('Carla', 0, 75, 40)
funcionario4 = FuncionarioTemporario('Denise', 0, 95, 44)

# Calcule e imprima o pagamento de cada funcionário usando o método calcular_pagamento().

print(f'O salário de {funcionario1.get_nome()} é igual a {funcionario1.calcular_pagamento()}')
print(f'O salário de {funcionario2.get_nome()} é igual a {funcionario2.calcular_pagamento()}')
print(f'O salário de {funcionario3.get_nome()} é igual a {funcionario3.calcular_pagamento()}')
print(f'O salário de {funcionario4.get_nome()} é igual a {funcionario4.calcular_pagamento()}')

# Dúvida ao final do exercício: Existe necessidade de criar um atributo "salario"?