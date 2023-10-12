saldo_conta = 0.0

valor_deposito = float(input())

if valor_deposito > 0:
    saldo_conta += valor_deposito
    print("Deposito realizado com sucesso!")
    print(f"Saldo atual: R$ {saldo_conta:.2f}")
elif valor_deposito == 0:
    print("Encerrando o programa...")
else:
    print("Valor invalido! Digite um valor maior que zero.")
