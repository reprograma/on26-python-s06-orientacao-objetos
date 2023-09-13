class pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome #atributo privado
        self.__idade = idade #atributo privado

    def get_nome(self):
        return self.__nome
    
    def set_nome(self, novo_valor):
        if len(novo_valor) > 0:
            self.__nome = novo_valor

    def get_idade(self):
        retun self.__idade