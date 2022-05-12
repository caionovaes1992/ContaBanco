
class Conta:

    # constrói e define o objeto através da função init (construção) e self (encontra o objeto na memória)
    def __init__(self, numero, titular, saldo, limite):
        print('Contruindo objeto... {}'.format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    # puxa um valor específico do objeto criado, acessando através da função self
    def extrato(self):
        print('Saldo de {} do titular {}'.format(self.__saldo, self.__titular))

    # adicionar (depositar) valores no saldo da conta
    def deposita(self, valor):
        self.__saldo += valor

    # o valor a ser sacado tem que ser menor que o saldo + limite
    def __pode_sacar(self, valor_a_sacar):
        saldo_disponivel = self.__saldo + self.__limite
        return valor_a_sacar <= saldo_disponivel

    # retirar (sacar) valores no saldo da conta
    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print('O valor {} passou o limite.'.format(valor))

    # transferir valor de uma conta para a outra
    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    # método com a unica responsabilidade de retornar o saldo da conta
    @property
    def saldo(self):
        return self.__saldo

    # método com a unica responsabilidade de retornar o titular da conta
    @property
    def titular(self):
        return self.__titular

    # método com a unica responsabilidade de retornar o limite da conta
    @property
    def limite(self):
        return self.__limite

    # método que aponta e altera o valor de algo no código, no caso o limite
    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    # desse forma deixamos estático o código do banco onde as contas serão criadas, sem precisar criar um objeto
    @staticmethod
    def codigo_banco():
        return '001'

    # método que retorna todos os códigos de bancos que podemos usar
    @staticmethod
    def codigos_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}