class Funcionario:
    def __init__(self, nome):
        self.nome = nome
        self.salario = 0.0

    def calcular_pagamento(self):
        pass

class FuncionarioTemporario(Funcionario):
    def __init__(self, nome, horas_trabalhadas, remuneracao_por_hora):
        super().__init__(nome)
        self.horas_trabalhadas = horas_trabalhadas
        self.remuneracao_por_hora = remuneracao_por_hora

    def calcular_pagamento(self):
        pagamento = self.horas_trabalhadas * self.remuneracao_por_hora
        return pagamento
    
class FuncionarioIntegral(Funcionario):
    def __init__(self, nome, salario_mensal):
        super().__init__(nome)
        self.salario_mensal = salario_mensal
    
    def calcular_pagamento(self):
        pagamento = self.salario_mensal
        return pagamento

#Exemplos para testar
 
pagamento_da_leticia = FuncionarioTemporario("Letícia Moreira", 120, 30)
print(pagamento_da_leticia.calcular_pagamento())

pagamento_da_samira = FuncionarioIntegral("Samira Leal", 5000)
print(pagamento_da_samira.calcular_pagamento())