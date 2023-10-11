saldo_Atual = float(input("Informe o saldo atual: "))
valor_Deposito = float(input("Informe o déposito: "))
valor_Retirada = float(input("Informe o valor da retirada: "))

#TODO: Calcular o saldo atualizado de acordo com a descrição deste desafio.
saldo_Atual += valor_Deposito - valor_Retirada
#TODO: Imprimir o a saída de conforme a tabela de exemplos (uma casa decimal).
print("Saldo atualizado na conta: {:.1f}".format(saldo_Atual))