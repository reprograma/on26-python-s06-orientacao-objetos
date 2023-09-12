class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    def get_nome(self):
        return self.__nome

    def set_idade(self, novo_valor):
        if novo_valor > 0:
            self.__nome = novo_valor
    
    def get_idade(self):
        return self.__idade

maria = Pessoa("Maria", 39)

print(maria.get_nome())

maria.set_idade(67)
print(maria.get_idade())