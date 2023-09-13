## 🧠 Exercício de Herança em Python: Sistema de Gerenciamento de Funcionários (Exercicío Avançado Extra)

# Você está encarregado de criar um sistema de gerenciamento de funcionários para uma empresa. 
# O sistema deve ser capaz de lidar com diferentes tipos de funcionários e calcular seus salários com 
# base em suas características específicas. 
# Para isso, você precisa implementar a hierarquia de classes apropriada usando herança em Python.

# Instruções:

# Crie uma classe base chamada Funcionario com os seguintes atributos:
#  - nome: o nome do funcionário.
#  - salario: o salário base do funcionário (inicialmente definido como 0).

# A classe Funcionario deve ter um método chamado `calcular_pagamento()` que retorna o pagamento do
# funcionário. No entanto, este método deve ser definido como um método abstrato (utilizando `pass`) 
# uma vez que cada tipo de funcionário (temporário e integral) calculará o pagamento de maneira diferente.

# Crie uma classe chamada FuncionarioTemporario, que herda da classe Funcionario. 
# Esta classe deve ter os seguintes atributos adicionais:

# - salario_por_hora: o salário por hora do funcionário temporário.
# - horas_trabalhadas: o número de horas trabalhadas pelo funcionário temporário.
# Na classe FuncionarioTemporario, implemente o método `calcular_pagamento()` para calcular o pagamento
# do funcionário temporário com base no salário por hora e nas horas trabalhadas.

# Crie uma classe chamada FuncionarioIntegral, que também herda da classe Funcionario. 
# Esta classe deve ter um atributo adicional:

# - salario_mensal: o salário mensal do funcionário integral.
# Na classe FuncionarioIntegral, implemente o método `calcular_pagamento()` para calcular o pagamento 
# do funcionário integral, que é igual ao seu salário mensal.

# Crie instâncias de FuncionarioTemporario e FuncionarioIntegral, atribuindo valores adequados aos 
# atributos de cada funcionário.

# Calcule e imprima o pagamento de cada funcionário usando o método `calcular_pagamento()`.


class Funcionario:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.salario = 0.0
    
    def calcular_pagamento(self):
        pass    
        
class FuncionarioTemporario(Funcionario):
    def __init__(self, nome, salario_hora, horas_trab):
        super().__init__(nome)
        self.salario_hora = salario_hora
        self.horas_trab = horas_trab
        
    def calcular_pagamento(self):
        return self.salario_hora * self.horas_trab
    
class FuncionarioIntegral(Funcionario):
    def __init__(self, nome, salario_mensal):
        super().__init__(nome)   
        self.salario_mensal = salario_mensal
        
    def calcular_pagamento(self):
        return self.salario_mensal
    
    
salario_deb_temporaria = FuncionarioTemporario ("Debora", 30, 100)
salario_jow_integral = FuncionarioIntegral("Joao", 3000)
    
print(salario_deb_temporaria.calcular_pagamento())
print(salario_jow_integral.calcular_pagamento())

    
# feito em grupo com: Andreza, Igea, Louise, Thaysa, Maria de Fatima, Marcinha