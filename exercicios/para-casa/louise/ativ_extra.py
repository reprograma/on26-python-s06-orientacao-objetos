class Funcionario:
    def __init__(self,nome):
        self.nome = str(nome)
        self.salario = 0

    def calcularPagamento(self):
        pass
    
class Temporario(Funcionario):
    def __init__(self,nome,salarioporhora,hora):
        self.nome = str(nome)
        self.salarioporhora = salarioporhora
        self.hora = hora
    
    def calcularPagamento(self):
        salario = self.salarioporhora * self.hora
        return salario
    
class FuncionarioIntegral(Funcionario):
    def __init__(self, nome, salariomensal):
        super().__init__(nome)
        self.salariomensal = salariomensal
    
    def calcularPagamento(self):
        return self.salariomensal

louise_funcionario = FuncionarioIntegral ('Marcinha Tabata',20.000)
igea_funcionario = Temporario ('Fatinha Rodrigues',1500, 10)

print (louise_funcionario.calcularPagamento())
print (igea_funcionario.calcularPagamento())