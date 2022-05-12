
class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    # property indica que estamos trabalhando com uma propriedade, indica nossa intenção de ter acesso ao objeto.
    @property
    # mesmo sem coloca-lo, aqui estamos usando o método get (com o @property não precisamos explicitar no código).
    def nome(self):
        print('Chamando @property nome()')
        return self.__nome.title() # método title() para sempre retornar o nome digitado com a primeira letra maiúscula, mesmo que tenha sido digitado minúsculo

    # mesmo sem coloca-lo, aqui estamos usando o método set (com o @property não precisamos explicitar no código).
    @nome.setter
    def nome(self, nome):
        print('Chamando setter nome()')
        self.__nome = nome
