

def cria_conta(numero, titular, saldo, limite): # para os valores não serem fixos, declaramos como variáveis da função
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

def deposita(conta, valor): # depositar incrementando valores no saldo da conta
    conta["saldo"] += valor

def saca(conta, valor): # nesse caso o saque irá retirar ao invés de incrementar um valor
    conta["saldo"] -= valor

def extrato(conta):  # imprime informações sobre a conta
    print("O saldo é {}.".format(conta["saldo"]))